import itertools
import json
import string
import time
from pathlib import Path

import pyzipper


class PasswordCracker:
    def __init__(self, config_path: Path, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.config = self._load_config(config_path)

        # Choose type and mode
        self.target_type: str = str(self.config.get("target_type", "string")).lower()
        self.target_value: str = str(self.config.get("target_value", "")).strip()
        self.mode = self.config.get("mode", "hybrid").lower()

        wordlist_name = self.config.get("wordlist_name", "100k_passwords.txt")
        self.wordlist_path = self.base_dir / "data" / wordlist_name
        self._common_words: set[str] = set()

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
            raise ValueError(f"Invalid JSON format in {path.name}: {e}")

    def _load_wordlist(self) -> None:
        """Loads the dictionary into a set for O(1) lookup."""
        if not self.wordlist_path.exists():
            print(f"[-] Wordlist file not found: {self.wordlist_path}")
            return

        try:
            start = time.perf_counter()
            with self.wordlist_path.open(
                "r", encoding="utf-8", errors="ignore"
            ) as file:
                self._common_words = {line.strip() for line in file if line.strip()}
            elapsed = time.perf_counter() - start
            print(f"[+] Loaded {len(self._common_words):,} words ({elapsed:.3f}s).")

        except Exception as e:  # noqa: BLE001
            print(f"[-] Failed to load dictionary: {e}")

    def verify_password(self, guess: str) -> bool:
        """Universal router checks: depending on target_type."""
        if self.target_type == "string":
            return guess == self.target_value

        if self.target_type == "zip":
            archive_path = self.base_dir / self.target_value
            try:
                with pyzipper.AESZipFile(archive_path) as zf:
                    first_file = zf.namelist()[0]
                    zf.read(first_file, pwd=guess.encode("utf-8"))
                    return True
            except Exception:  # noqa: BLE001
                return False

        return False

    def check_dictionary(self) -> str | None:
        """Checks for the presence of the password in the dictionary."""
        if not self._common_words:
            print("[-] Dictionary is empty or missing.")
            return None

        print(f"[*] Starting dictionary search (Target type: {self.target_type})...")
        start_time = time.perf_counter()

        for word in self._common_words:
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
            min_len = self.config.get("min_length", 1)
            max_len = self.config.get("max_length", 5)
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

        valid_targets = ("string", "zip")
        if self.target_type not in valid_targets:
            print(
                f"[-] Unsupported target_type '{self.target_type}'. Use: {valid_targets}"
            )
            return

        if self.target_type == "zip":
            archive_path = self.base_dir / self.target_value
            if not archive_path.exists():
                print(f"[-] Target ZIP archive not found: {archive_path}")
                return

        valid_modes = ("dictionary_only", "bruteforce_only", "hybrid")
        if self.mode not in valid_modes:
            print(f"[-]] Invalid mode '{self.mode}'. Supported modes: {valid_modes}")
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
    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.json"

    try:
        cracker = PasswordCracker(config_path=config_path, base_dir=base_dir)
        cracker.run()
    except Exception as e:  # noqa: BLE001
        print(f"[-] Fatal Error: {e}")


if __name__ == "__main__":
    main()
