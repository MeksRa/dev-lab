import hashlib
from dataclasses import InitVar, dataclass
from typing import ClassVar


@dataclass
class UserAccount:
    username: str

    # -- convert to a hash without saving -- (InitVar)
    raw_password: InitVar[str]
    # --

    password_hash: str = ""
    is_active: bool = True

    # (ClassVar) class atribute for all objects in this class
    MIN_USERNAME_LENGTH: ClassVar[int] = 3

    def __post_init__(self, raw_password: str) -> None:
        if len(self.username) < self.MIN_USERNAME_LENGTH:
            raise ValueError(f"Login should be shorter than {self.MIN_USERNAME_LENGTH}")

        if not self.is_valid_password(raw_password):
            raise ValueError("Password is too simple! Min 6 symbols")

        # -- convert to a hash, saves hash -- (InitVar)
        self.password_hash = self._hash_password(raw_password)
        # --

    # (@staticmethod)  # you don't need 'self' here, this is an isolated method
    @staticmethod
    def is_valid_password(password: str) -> bool:
        """auxiliary method, only checks length, doesn't affect the class"""
        return len(password) >= 6

    @staticmethod
    def _hash_password(password: str) -> str:
        """hash using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    # (@classmethod)
    @classmethod
    def from_string(cls, data_string: str) -> "UserAccount":
        """Alternative constructor: creates an object from a string in the format 'login:password'."""
        username, raw_password = data_string.split(":")
        return cls(username=username, raw_password=raw_password)

    # (@property)
    @property
    def masked_username(self) -> str:
        """Dynamic property: masks the middle of the login with asterisks."""
        if len(self.username) <= 2:
            return self.username
        return f"{self.username[0]}***{self.username[-1]}"

    def check_password(self, password_to_check: str) -> bool:
        """Checks whether the entered password matches the stored hash."""
        return self.password_hash == self._hash_password(password_to_check)


def main() -> None:
    user1: UserAccount = UserAccount(username="MeksRa_dev", raw_password="123456")
    print(user1)
    # UserAccount(username='MeksRa_dev', password_hash='8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', is_active=True)
    print(f"Masked login: {user1.masked_username}")  # Masked login: M***v
    print(
        f"Check password: qwerty {user1.check_password('qwerty')}"
    )  # Check password: qwerty False
    print(
        f"Check password: 123456 {user1.check_password('123456')}"
    )  # Check password: 123456 True

    user2: UserAccount = UserAccount.from_string("MeksRa_dev_2:1234567890")
    print(
        f"Successfully created user: {user2.username}"
    )  # Successfully created user: MeksRa_dev_2

    try:
        bad_user = UserAccount(username="al", raw_password="123")  # noqa: F841
    except ValueError as e:
        print(
            f"Validation Error: {e}"
        )  # Validation Error: Login should be shorter than 3


if __name__ == "__main__":
    main()
