import io
import itertools
import json
import multiprocessing as mp
import string
import time
from pathlib import Path

import msoffcrypto
import py7zr
import pypdf
import pyzipper
import rarfile


def _worker_check_password(args: tuple) -> str | None:
    """Worker function executed across multiple CPU process pools for fast targets."""
    word, target_type, target_value, base_dir = args

    # 01) String
    if target_type == "string":
        return word if word == target_value else None

    target_file_path = base_dir / target_value

    # 2) ZIP (.zip)
    if target_type == "zip":
        try:
            with pyzipper.AESZipFile(target_file_path) as zf:
                first_file = zf.namelist()[0]
                zf.read(first_file, pwd=word.encode("utf-8"))
                return word
        except Exception:  # noqa: BLE001
            return None

    return None


class PasswordCracker:
    def __init__(self, config_path: Path, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.config = self._load_config(config_path)

        # Choose type and mode
        self.target_type: str = str(self.config.get("target_type", "string")).lower()
        self.target_value: str = str(self.config.get("target_value", "")).strip()
        self.mode = str(self.config.get("mode", "hybrid")).lower()

        wordlist_name = str(self.config.get("wordlist_name", "100k_passwords.txt"))
        self.wordlist_path = self.base_dir / "data" / wordlist_name
        self._common_words: list[str] = []

        if self.mode in ("dictionary_only", "hybrid"):
            self._load_wordlist()

    def _load_config(self, path: Path) -> dict:
        """Loads config.json."""
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        try:
            with path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {path.name}: {e}") from e

    def _load_wordlist(self) -> None:
        """Loads the dictionary into a list to preserve ordering."""
        if not self.wordlist_path.exists():
            print(f"[-] Wordlist file not found: {self.wordlist_path}")
            return

        try:
            start = time.perf_counter()
            with self.wordlist_path.open(
                "r", encoding="utf-8", errors="ignore"
            ) as file:
                # Retain list ordering instead of set hashing
                self._common_words = [line.strip() for line in file if line.strip()]
            elapsed = time.perf_counter() - start
            print(f"[+] Loaded {len(self._common_words):,} words ({elapsed:.3f}s).")

        except Exception as e:  # noqa: BLE001
            print(f"[-] Failed to load dictionary: {e}")

    def verify_password(self, guess: str) -> bool:
        """Universal router checks: depending on target_type."""

        # 01) String
        if self.target_type == "string":
            return guess == self.target_value

        target_file_path = self.base_dir / self.target_value

        # 2) ZIP (.zip)
        if self.target_type == "zip":
            try:
                with pyzipper.AESZipFile(target_file_path) as zf:
                    first_file = zf.namelist()[0]
                    zf.read(first_file, pwd=guess.encode("utf-8"))
                    return True
            except Exception:  # noqa: BLE001
                return False

        # 3) 7-Zip (.7z)
        if self.target_type == "7z":
            try:
                with py7zr.SevenZipFile(
                    target_file_path, mode="r", password=guess
                ) as szf:
                    return szf.testzip() is None
            except Exception:  # noqa: BLE001
                return False

        # 4) RAR (.rar)
        if self.target_type == "rar":
            try:
                with rarfile.RarFile(target_file_path) as rf:
                    rf.setpassword(guess)
                    info = rf.infolist()[0]
                    with rf.open(info) as fp:
                        fp.read(1)
                    return True
            except Exception:  # noqa: BLE001
                return False

        # 5) PDF
        if self.target_type == "pdf":
            try:
                reader = pypdf.PdfReader(target_file_path)
                if not reader.is_encrypted:
                    return True
                return bool(reader.decrypt(guess))
            except Exception:  # noqa: BLE001
                return False

        # 6) Microsoft Office (.docx, .xlsx, .pptx, etc.)
        if self.target_type == "office":
            try:
                with open(target_file_path, "rb") as f:
                    office_file = msoffcrypto.OfficeFile(f)
                    office_file.load_key(password=guess)
                    dummy = io.BytesIO()
                    office_file.decrypt(dummy)
                    return True
            except Exception:  # noqa: BLE001
                return False

        return False

    def check_dictionary(self) -> str | None:
        """Checks for the presence of the password in the dictionary."""
        if not self._common_words:
            print("[-] Dictionary is empty or missing.")
            return None

        # Parallel search for fast targets
        if self.target_type in ("string", "zip"):
            cpu_count = mp.cpu_count()
            print(
                f"[*] Starting parallel dictionary search across {cpu_count} CPU cores..."
            )
            start_time = time.perf_counter()

            tasks = [
                (word, self.target_type, self.target_value, self.base_dir)
                for word in self._common_words
            ]

            with mp.Pool(processes=cpu_count) as pool:
                for result in pool.imap_unordered(
                    _worker_check_password, tasks, chunksize=1000
                ):
                    if result:
                        pool.terminate()
                        elapsed = time.perf_counter() - start_time
                        return (
                            f"\n[!] MATCH FOUND IN DICTIONARY!\n"
                            f"    Target: '{self.target_value}' ({self.target_type})\n"
                            f"    Password: '{result}'\n"
                            f"    Time elapsed: {elapsed:.2f}s"
                        )
        else:
            # Sequential search with progress logging for heavy formats (rar, pdf, 7z, office)
            print(
                f"[*] Starting sequential dictionary search for '{self.target_type}'..."
            )
            start_time = time.perf_counter()

            for i, word in enumerate(self._common_words, 1):
                if i % 1000 == 0:
                    elapsed = time.perf_counter() - start_time
                    speed = i / elapsed if elapsed > 0 else 0
                    print(
                        f"[*] Checked {i:,}/{len(self._common_words):,} words | Speed: {speed:,.0f} words/sec"
                    )

                if self.verify_password(word):
                    elapsed = time.perf_counter() - start_time
                    return (
                        f"\n[!] MATCH FOUND IN DICTIONARY!\n"
                        f"    Target: '{self.target_value}' ({self.target_type})\n"
                        f"    Password: '{word}'\n"
                        f"    Time elapsed: {elapsed:.2f}s"
                    )

        print("[-] Target password not found in dictionary.")
        return None

    def brute_force(self) -> str | None:
        """Iterates through combinations of symbols of a specified length."""
        charset = string.ascii_lowercase
        if self.config.get("use_uppercase"):
            charset += string.ascii_uppercase
        if self.config.get("use_digits"):
            charset += string.digits
        if self.config.get("use_symbols"):
            charset += string.punctuation

        try:
            min_len = int(self.config.get("min_length", 1))
            max_len = int(self.config.get("max_length", 5))
        except ValueError:
            print("[-] Invalid length settings in config.json. Must be integers.")
            return None

        if min_len < 1 or max_len < min_len:
            print("[-] Invalid length bounds (min_length > max_length or < 1).")
            return None

        attempts = 0
        start_time = time.perf_counter()

        print(f"[*] Starting brute-force (length: {min_len}-{max_len})...")
        print(f"[*] Charset size: {len(charset)} characters.")

        for length in range(min_len, max_len + 1):
            for tuple_guess in itertools.product(charset, repeat=length):
                attempts += 1
                guess = "".join(tuple_guess)

                if attempts % 10000 == 0:
                    elapsed = time.perf_counter() - start_time
                    speed = attempts / elapsed if elapsed > 0 else 0
                    print(
                        f"[*] Progress: {attempts:,} attempts | "
                        f"Current guess: '{guess}' | Speed: {speed:,.0f} att/sec"
                    )

                if self.verify_password(guess):
                    elapsed = time.perf_counter() - start_time
                    speed = attempts / elapsed if elapsed > 0 else 0
                    return (
                        f"\n[+] SUCCESS! Password cracked!\n"
                        f"    Target: '{self.target_value}' ({self.target_type})\n"
                        f"    Password: '{guess}'\n"
                        f"    Attempts: {attempts:,}\n"
                        f"    Time elapsed: {elapsed:.2f}s\n"
                        f"    Speed: {speed:,.0f} attempts/sec"
                    )

        elapsed = time.perf_counter() - start_time
        print(f"[-] Password not found after {attempts:,} attempts ({elapsed:.2f}s).")
        return None

    def run(self) -> None:
        """Starts the process according to the selected mode."""
        if not self.target_value:
            print("[-] Error: 'target_value' in config.json is empty.")
            return

        valid_targets = ("string", "zip", "7z", "rar", "pdf", "office")
        if self.target_type not in valid_targets:
            print(
                f"[-] Unsupported target_type '{self.target_type}'. Use: {valid_targets}"
            )
            return

        if self.target_type != "string":
            target_file_path = self.base_dir / self.target_value
            if not target_file_path.exists():
                print(f"[-] Target file not found: {target_file_path}")
                return

        valid_modes = ("dictionary_only", "bruteforce_only", "hybrid")
        if self.mode not in valid_modes:
            print(f"[-] Invalid mode '{self.mode}'. Supported modes: {valid_modes}")
            return

        print(
            f"=== Password Cracker Started (Target: {self.target_type} | Mode: {self.mode}) ==="
        )
        start_total = time.perf_counter()

        # 1) DICTIONARY -> (Only dictionary)
        if self.mode == "dictionary_only":
            if result := self.check_dictionary():
                print(result)

        # 2) BRUTEFORCE -> (Only bruteforce)
        elif self.mode == "bruteforce_only":
            if result := self.brute_force():
                print(result)

        # 3) HYBRID -> (Dictionary, if nothing found - bruteforce)
        elif self.mode == "hybrid":
            result = self.check_dictionary()
            if result:
                print(result)
            else:
                if result_bf := self.brute_force():
                    print(result_bf)

        total_elapsed = time.perf_counter() - start_total
        print(f"\n[=] Total execution time: {total_elapsed:.4f}s")


def main() -> None:
    """Entry point. Settings are managed in config.json."""
    rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\UnRAR.exe"
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"

    try:
        cracker = PasswordCracker(config_path=config_path, base_dir=base_dir)
        cracker.run()
    except Exception as e:  # noqa: BLE001
        print(f"[-] Fatal Error: {e}")


if __name__ == "__main__":
    mp.freeze_support()
    main()
