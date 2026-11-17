from typing import override


class Pet:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        """Returns general pet formatted status-string"""
        return f"Name: {self.name}. Age: {self.age}"

    def speak(self) -> str:
        """Simulates general pet speaking"""
        return "I don't know what to say..."


class Cat(Pet):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.color = color

    @override
    def show(self) -> str:
        """Returns formatted status-string"""
        base_str = super().show()
        return f"{base_str}. Color: {self.color}"

    @override
    def speak(self) -> str:
        """Simulates cats meowing"""
        return "Meow"


class Dog(Pet):
    @override
    def speak(self) -> str:
        """Simulates dogs barking"""
        return "Bark"


def main() -> None:
    p = Pet("Tim", 19)
    c = Cat("Bill", 34, "Orange")
    d = Dog("Jill", 25)
    print(p.speak())
    print(p.show())
    print(c.speak())
    print(c.show())
    print(d.speak())
    print(d.show())


if __name__ == "__main__":
    main()
