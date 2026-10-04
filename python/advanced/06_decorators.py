import time
from collections.abc import Callable
from functools import wraps
from typing import Any

# Creating our own decorators


def get_time(func: Callable) -> Callable:  # Decorator
    """Times how long it takes to execute a function."""

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        """All of the functionality that belongs to the decorator should go inside the wrapper"""
        start_time: float = time.perf_counter()
        func(*args, **kwargs)
        end_time: float = time.perf_counter()

        print(f"Time: {end_time - start_time:.3f}s")

    return wrapper


@get_time  # This will apply the functionality of our decorator to this func
def calculate() -> None:
    """calculate() docstring  ... Just a random func that does something"""
    print("Calculating...")
    for i in range(20_000_000):
        pass
    print("Done")


# ------------------------------------


def repeat(number: int) -> Callable:
    """Repeat a function call x amount of times"""

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            value: Any = None
            for _ in range(number):
                value = func(*args, **kwargs)

            return value

        return wrapper

    return decorator


@repeat(number=3)
def greet_and_add(name: str, a: int, b: int) -> int:
    """A function used to greet people"""
    print(f"Hello, {name}!")
    print(f"{a+b=}")
    return a + b


def main() -> None:
    calculate()
    # Output:
    # Calculating...
    # Done
    # Time: 0.246s

    # without @wraps(func)
    print(calculate.__name__)
    # wrapper
    print(calculate.__doc__)
    # All of the functionality that belongs to the decorator should go inside the wrapper  # without @wraps

    # with @wraps(func)
    print(calculate.__name__)
    # calculate
    print(calculate.__doc__)
    # calculate() docstring  ... Just a random func that does something

    # ------------------------------------

    greet_and_add("MeksRa", 50, 60)
    # Output:
    # Hello, MeksRa!
    # a+b=110
    # Hello, MeksRa!
    # a+b=110
    # Hello, MeksRa!
    # a+b=110
    print(greet_and_add.__name__)  # greet_and_add
    print(greet_and_add.__doc__)  # A function used to greet people


if __name__ == "__main__":
    main()
