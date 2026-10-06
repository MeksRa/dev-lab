from collections.abc import Callable, Iterable, Sequence
from typing import Any, Final, Protocol

# ==========================================
# 19. Any
# Disables type checking for the variable
# ==========================================
data: Any = "hello"
data = 42  # Type checker will not flag this
data.foo_bar()  # Suppresses type checker errors


# ==========================================
# 20. Final
# Prevents reassigning variables or overriding
# ==========================================
MAX_USERS: Final = 100
# MAX_USERS = 200  # Error: Cannot reassign a Final variable


# ==========================================
# 21. Iterables
# Best for input args that are only looped over
# ==========================================
def print_all(items: Iterable[int]) -> None:
    for item in items:
        print(item)


print_all([1, 2, 3])  # Accepts list, tuple, set, generator, etc.


# ==========================================
# 22. Sequences
# Ordered collections with index access [i] & len()
# ==========================================
def get_first(items: Sequence[str]) -> str:
    return items[0]  # Supports indexing and len(), but immutable operations only


get_first(("a", "b"))  # Works with list/tuple, but NOT set


# ==========================================
# 23. Callables
# For function parameters: [[arg_types], return_type]
# ==========================================
def apply_op(a: int, b: int, func: Callable[[int, int], int]) -> int:
    return func(a, b)


result = apply_op(2, 3, lambda x, y: x + y)


# ==========================================
# 24. Protocols
# Structural typing (duck typing) without explicit inheritance
# ==========================================
class Renderable(Protocol):
    def render(self) -> str: ...  # Minimum required interface contract


class Card:
    def render(self) -> str:
        return "Card HTML"  # No need to inherit from Renderable


def draw(obj: Renderable) -> None:
    print(obj.render())


draw(Card())
