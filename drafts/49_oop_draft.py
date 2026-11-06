import re
from typing import Self


class User:
    MIN_PASSWORD_LENGTH = 6

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
        self.is_active: bool = True

    def deactivate(self) -> None:
        self.is_active = False
        print(f"User '{self.username}' has been deactivated.")

    def __str__(self) -> str:
        status = "Active" if self.is_active else "Inactive"
        return f"User: {self.username} ({self.email}) - [{status}]"

    @classmethod
    def from_csv_string(cls, csv_line: str) -> Self:
        """Creates a User object from a string in the format 'username,email'."""
        username, email = csv_line.strip().split(",")
        print("Creating a user from a csv string...")
        return cls(username=username, email=email)

    @staticmethod
    def is_strong_password(password: str) -> bool:
        """Checks whether the password is secure"""
        if len(password) < User.MIN_PASSWORD_LENGTH:
            return False
        return bool(re.search(r"\d", password))


def main() -> None:
    user1 = User("user_max", "max@gmail.com")
    print(user1)
    print("-" * 20)

    raw_data = "bob_code,bob@gmail.com"
    user2 = User.from_csv_string(raw_data)
    print(user2)
    print("-" * 20)

    passwords_to_test = ["123", "qwerty", "secure123"]

    for pwd in passwords_to_test:
        is_valid = User.is_strong_password(pwd)
        print(f"Is the password '{pwd}' secured? -> {is_valid}")


if __name__ == "__main__":
    main()
