import itertools
import json
import string
import time
from pathlib import Path


class PasswordCracker:
    def __init__(self, config_path: Path, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.config = self._load_config(config_path)

        self.target = str(self.config.get("target_password", "")).strip()
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

    def check_dictionary(self) -> bool:
        """Checks for the presence of the password in the dictionary."""
        if not self._common_words:
            print("[-] Dictionary is empty or missing.")
            return False

        print("[*] Starting dictionary search...")

        if self.target in self._common_words:
            print(f"[!] MATCH FOUND IN DICTIONARY: '{self.target}'")
            return True

        print("[-] Target password not found in dictionary.")
        return False

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

                if guess == self.target:
                    elapsed = time.perf_counter() - start_time
                    speed = attempts / elapsed if elapsed > 0 else 0
                    return (
                        f"\n[+] SUCCESS! Password cracked: '{guess}'\n"
                        f"____Attempts: {attempts:,}\n"
                        f"____Time elapsed: {elapsed:.2f}s\n"
                        f"____Speed: {speed:,.0f} passwords/sec"
                    )

        elapsed = time.perf_counter() - start_time
        print(f"[-] Password not found after {attempts:,} attempts ({elapsed:.2f}s).")
        return None

    def run(self) -> None:
        """Starts the process according to the selected mode."""
        if not self.target:
            print("[-] Error: 'target_password' in config.json is empty.")
            return

        valid_modes = ("dictionary_only", "bruteforce_only", "hybrid")
        if self.mode not in valid_modes:
            print(f"[-]] Invalid mode '{self.mode}'. Supported modes: {valid_modes}")
            return

        print(f"=== Password Cracker Started (Mode: {self.mode}) ===")
        start_total = time.perf_counter()

        # 1) DICTIONARY -> (Only dictionary)
        if self.mode == "dictionary_only":
            self.check_dictionary()

        # 2) BRUTEFORCE -> (Only bruteforce)
        elif self.mode == "bruteforce_only":
            if result := self.brute_force():
                print(result)

        # 3) HYBRID -> (Dictionary, if nothing found - bruteforce)
        elif self.mode == "hybrid":
            found = self.check_dictionary()
            if not found and (result := self.brute_force()):
                print(result)

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
