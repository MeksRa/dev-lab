from typing import TypedDict, Unpack, override


# ==========================================
# 34. @override
# Explicitly marks a method as overriding a base class method.
# Pylance throws an error if the parent method doesn't exist or signature mismatches.
# ==========================================
class Parent:
    def greet(self) -> None:
        print("Hello from Parent")


class Child(Parent):
    @override
    def greet(self) -> None:
        print("Hello from Child")


# ==========================================
# 35. type (type[T])
# Used to annotate class objects themselves, rather than instances of classes.
# ==========================================
class Animal:
    pass


class Dog(Animal):
    pass


def create_instance(cls: type[Animal]) -> Animal:
    return cls()  # Accepts the class 'Dog' or 'Animal', returns an instance


dog_instance = create_instance(Dog)

# --- ---

# Example: TypeAlias = str | int
# Example2: TypeAlias = tuple[float, float]

# Use 'type ...' instead of "TypeAlias"

type Example = str | int
type Example2 = tuple[float, float]

# --- ---

# Modern 'type' syntax with generic type parameters [T]

# Generic type alias: T can be replaced with any type later
type ListOrDict[T] = list[T] | dict[str, T]

# Usage with int (T = int)
user_scores: ListOrDict[int] = [10, 20, 30]

# Usage with str (T = str)
user_names: ListOrDict[str] = {"admin": "Alice", "guest": "Bob"}


# Generic function parameter: T preserves the exact type for Pylance/mypy
def get_first[T](items: list[T]) -> T:
    return items[0]


first_num: int = get_first([1, 2, 3])  # Pylance knows this returns int
first_str: str = get_first(["a", "b"])  # Pylance knows this returns str


# ==========================================
# 36. Unpack
# Unpacks a TypedDict into **kwargs function parameters for typed keyword arguments.
# ==========================================
class Options(TypedDict):
    host: str
    port: int


def connect(**kwargs: Unpack[Options]) -> None:
    print(f"Connecting to {kwargs['host']}:{kwargs['port']}")


# Called using keyword arguments matching the TypedDict keys:
connect(host="localhost", port=8000)
