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


# ==================
# 02) f-strings
# ==================

var: int = 10


def add(a: int, b: int) -> int:
    return a + b


print(f"{var=}")  # var=10
print(f"{add(5, 10)=}")  # add(5, 10)=15

big_number: float = 123456789
print(f"{big_number:,}")  # 123,456,789  # ',' -> thousand separator
print(f"{big_number:_}")  # 123_456_789  # '_' -> thousand separator
fraction: float = 1234.5678
print(f"{fraction:.2f}")  # 1234.57  # round to 2 decimals as a float
print(f"{fraction:,.3f}")  # 1,234.568  # round to 3 + thousand sep
percent: float = 0.5
percent_second: float = 0.5555555555555
print(f"{percent: .2%}")  #  50.00%
print(f"{percent: .0%}")  #  50%
print(f"{percent_second: .3%}")  #  55.556%

second_var: str = "Bob"
print(f"{second_var:10}: Hello")  # Bob       : Hello  # -> bob(3) + 7 spaces
print(f"{second_var:>10}: Hello")  #        Bob: Hello
print(f"{second_var:^10}: Hello")  #    Bob    : Hello
print(f"{second_var:_>10}: Hello")  # _______Bob: Hello  # "_" -> any symbol could be
print(f"{second_var:_<10}: Hello")  # Bob_______: Hello
print(f"{second_var:#^10}: Hello")  # ###Bob####: Hello

numbers: list[int] = [1, 100, 1_000, 10_000]
for number in numbers:
    print(f"{number:_>5}: counting!")
# ____1: counting!
# __100: counting!
# _1000: counting!
# 10000: counting!

user: str = "MeksRa"
path: str = r"\Users\MeksRa\..."  # raw string
path: str = rf"\Users\{user}\..."  # f + r string
print(path)  # \Users\MeksRa\...


def main() -> None:
    # 01 =======doc======== 01

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

    # 02 ========f========= 02


if __name__ == "__main__":
    main()
