# 99-100

# ==================
# 01) Docstrings
# ==================

"""
This is a docstring
U'll see this when u hover over this module name
"""


class User:
    """
    When you hover over this class,
    you see the description
    we wrote in the docstrings.
    """

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def show_id(self) -> None:
        """Prints the user_id"""
        print(self.user_id)


def user_exists(user: User, database: set[User]) -> bool:
    """Checks if a user is inside a database

    Args:
        user: The user to check for.
        database: the database to check inside.
    Returns:
        bool: True if user exists, False otherwise.
    """
    return user in database


def main() -> None:
    user: User = User(3)
    user.show_id()

    bob: User = User(0)
    anna: User = User(1)
    database: set[User] = {bob, anna}
    if user_exists(bob, database):
        print("User exists in database!")
    else:
        print("No user found...")

    print(User.__doc__)
    print(user_exists.__doc__)


if __name__ == "__main__":
    main()
