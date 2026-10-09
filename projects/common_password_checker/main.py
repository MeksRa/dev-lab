from pathlib import Path


def load_common_passwords(file_path: Path) -> dict[str, int]:
    """Loads a password dictionary and stores their ranking (position)."""
    passwords: dict[str, int] = {}

    with file_path.open("r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            passwords[line.strip()] = index
    return passwords


def check_password(password: str, common_passwords: dict[str, int]) -> None:
    """Checks the password in O(1) time and outputs its weakness rating.\n
    (Ranking of the 100,000 most common passwords)"""
    if password in common_passwords:
        rank = common_passwords[password]
        print(f"{password}: ❌ #{rank} in common passwords list")
    else:
        print(f"{password}: ✅ Unique password!")


def main() -> None:
    """
    Entry point. Initialize path to txt file.
    \nSourced from:\n
    https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt
    """
    base_dir = Path(__file__).parent
    data_file = base_dir / "data" / "100k_passwords.txt"

    common_passwords = load_common_passwords(data_file)
    print(common_passwords)
    user_password: str = input("Enter a password: ").strip()
    check_password(user_password, common_passwords)


if __name__ == "__main__":
    main()
