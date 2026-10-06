# ==========================================
# 5. Basic types
# Built-in primitive types
# ==========================================
age: int = 25
price: float = 19.99
name: str = "Alice"
is_active: bool = True


# ==========================================
# 6. Union types
# Variable can hold one of several types (| operator)
# ==========================================
user_id: int | str = 101
user_id = "usr_101"  # Valid for both int and str


# ==========================================
# 7. Lists
# Mutable collections of items of a specific type
# ==========================================
scores: list[int] = [90, 85, 88]
scores.append(92)


# ==========================================
# 8. Tuples
# Fixed-size ordered sequences (can specify exact element types)
# ==========================================
point: tuple[int, int] = (10, 20)
user_info: tuple[str, int, bool] = ("Bob", 30, True)


# ==========================================
# 9. Sets
# Unordered collections of unique elements
# ==========================================
unique_tags: set[str] = {"python", "coding"}


# ==========================================
# 10. Dictionaries
# Key-value pairs with homogeneous key/value types
# ==========================================
user_ages: dict[str, int] = {"Alice": 25, "Bob": 30}


# ==========================================
# 11. Optionals
# Values that can be of a specific type or None
# ==========================================
email: str | None = None  # Equivalent to Optional[str]
email = "user@example.com"


# ==========================================
# 12. Classes
# Using custom classes as type annotations
# ==========================================
class User:
    def __init__(self, username: str) -> None:
        self.username = username


current_user: User = User("alice_dev")


# ==========================================
# 13. Return types
# Annotating function return values (use None for functions without return)
# ==========================================
def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"


def log_message(msg: str) -> None:
    print(f"[LOG]: {msg}")


# ==========================================
# 14. External types
# Importing types from external libraries or standard modules
# ==========================================
from datetime import datetime

current_time: datetime = datetime.now().astimezone()
