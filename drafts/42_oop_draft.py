from typing import override


class Pet:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        return f"Name: {self.name}. Age: {self.age}"

    def speak(self) -> str:
        return "I don't know what to say..."


class Cat(Pet):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(name, age)
        self.color = color

    @override
    def show(self) -> str:
        base_str = super().show()
        return f"{base_str}. Color: {self.color}"

    @override
    def speak(self) -> str:
        return "Meow"


class Dog(Pet):
    @override
    def speak(self) -> str:
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
