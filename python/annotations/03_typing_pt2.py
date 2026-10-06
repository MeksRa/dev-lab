from collections.abc import Generator, Iterator
from typing import Literal, NewType, Self, TypeAlias

# ==========================================
# 29. Literals
# Restricts values to specific exact literal values
# ==========================================
Mode: TypeAlias = Literal["r", "w", "a"]
current_mode: Mode = "r"  # u can use only "r", "w" or "a".


def open_file(mode: Mode) -> None:
    print(f"Opening file in {mode} mode")


open_file("r")  # u can use only "r", "w" or "a".


# ==========================================
# 30. TypeAlias
# Creates a readable alias for complex type signatures
# ==========================================
# Python 3.10+ syntax with TypeAlias (or Python 3.12+ 'type UserId = int | str')
UserId: TypeAlias = int | str  # Created alias
user_db: dict[UserId, str] = {101: "Alice", "usr_102": "Bob"}


# ==========================================
# 31. NewType
# Creates a distinct subtype to prevent mixing up identical base types
# ==========================================
UserIdNum = NewType("UserIdNum", int)
OrderNum = NewType("OrderNum", int)

user_id = UserIdNum(42)
order_id = OrderNum(42)


def process_user(u_id: UserIdNum) -> None:
    print(f"User ID: {u_id}")


process_user(user_id)
# process_user(order_id)  # Error: Expected UserIdNum, got OrderNum


# ==========================================
# 32. Self
# Annotates methods returning an instance of their own class (e.g., method chaining)
# ==========================================
class Builder:
    def set_name(self, name: str) -> Self:
        self.name = name
        return self


builder = Builder().set_name("MyBuilder")


# ==========================================
# 33. Generators
# Annotates generator functions: Generator[YieldType, SendType, ReturnType]
# ==========================================
def count_up_gen(to: int) -> Generator[int, None, None]:
    count = 1
    while count <= to:
        yield count
        count += 1


for num in count_up_gen(3):
    print(num)


# ==========================================
# 34. Iterators
# Simple alternative using Iterator[YieldType]
# ==========================================
def count_up_iter(to: int) -> Iterator[int]:
    count = 1
    while count <= to:
        yield count
        count += 1


for num in count_up_iter(3):
    print(num)
