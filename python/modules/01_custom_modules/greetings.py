from typing import Final

AUTHOR: Final[str] = "Federico"
VERSION: Final[int] = 1

def greet(name: str) -> None:
    print(f"Hello, {name}!")