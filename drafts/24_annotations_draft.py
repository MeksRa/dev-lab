from collections.abc import Callable, Sequence
from typing import Any, Final, Protocol

# Exercise 1
CONSTANT: Final[int] = 2


# Exercise 2
def get_repr(obj: Any) -> str:
    return repr(obj)


my_repr: str = get_repr("I love typing!")
print(my_repr)

# Exercise 3
numbers: list[int] = [20, 5, 30, 100]


def get_first_element(elements: Sequence[int]) -> int:
    return elements[0] if elements else -1


print(get_first_element(numbers))


# Exercise 4:
def say_hello(person: str, greeting: str) -> None:
    print(f"{greeting}, {person}!")


def greet(
    people: list[str], greeting: str, hello_func: Callable[[str, str], None]
) -> None:
    for person in people:
        hello_func(person, greeting)


friends: list[str] = ["Mario", "Luigi", "James"]
greet(friends, "Yo", say_hello)


# Exercise 5:
class Camera(Protocol):
    def take_picture(self) -> str: ...

    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...


def automate_photo(camera: Camera) -> str:
    camera.turn_on()
    photo: str = camera.take_picture()
    camera.turn_off()

    return photo


class Canon:
    def __init__(self, name: str) -> None:
        self.name = name

    def take_picture(self) -> str:
        print(f"{self.name} took a picture!")
        return "image.jpg"

    def turn_on(self) -> None:
        print(f"Turning on {self.name}.")

    def turn_off(self) -> None:
        print(f"Turning off {self.name}...")


my_camera: Canon = Canon("CanonDigital")
automate_photo(my_camera)
