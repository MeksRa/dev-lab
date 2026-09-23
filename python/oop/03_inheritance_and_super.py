from typing import override  # only for 02) super() block

# 01) Inheritance ==================================


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def drink(self) -> None:
        print(f"{self.name} is drinking")

    def eat(self) -> None:
        print(f"{self.name} is eating")


# tell python that we want to use Animal as a base class, parent class
class Dog(Animal):  # Enter class Animal in parentenses for inheritance
    # === We can Delete this block. super() needs only if we add unique attributes === #
    def __init__(self, name: str) -> None:
        super().__init__(name)  # super() just refers to the parent class (Animal)

    # === We can Delete this block. super() needs only if we add unique attributes === #

    def bark(self) -> None:
        print(f"{self.name}: bark bark!")

    def routine(self) -> None:
        self.eat()  # We took it(inherited) from class Animal
        self.bark()
        self.drink()  # We took it(inherited) from class Animal


# tell python that we want to use Animal as a base class, parent class
class Cat(Animal):  # Enter class Animal in parentenses for inheritance
    # === We can Delete this block. super() needs only if we add unique attributes === #
    def __init__(self, name: str) -> None:
        super().__init__(name)  # super() just refers to the parent class (Animal)

    # === We can Delete this block. super() needs only if we add unique attributes === #

    def meow(self) -> None:
        print(f"{self.name}: meow meow!")


# 02) super() ==================================


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides

    def describe(self) -> None:  # 1
        print(f"{self.name} ({self.sides} sides)")

    def shape_method(self) -> None:
        print(f"{self.name}: shape_method()")


class Square(Shape):  # inherits from Shape, as you can see
    def __init__(self, size: float) -> None:
        super().__init__("Square", 4)  # Old args Back to the parent class Shape
        self.size = size  # Save new args

    @override  # type annotation  # Mark that and Python will know that you're overriding this on purpose
    def describe(self) -> None:  # 2
        print(f"I am a {self.name} with a size of {self.size}")


class Rectangle(Shape):
    def __init__(self, length: float, height: float) -> None:
        super().__init__("Rectangle", 4)
        self.length = length
        self.height = height

    @override  # type annotation  # Mark that and Python will know that you're overriding this on purpose
    def describe(self) -> None:  # 3
        print(f"{self.name}: ({self.height}x{self.length})")


def main() -> None:
    # 01) Inheritance
    dog: Dog = Dog("Jack(dog)")
    cat: Cat = Cat("Destroyer of Worlds(cat)")

    dog.bark()  # as you can see, we have unique method .bark and all other methods from animal
    cat.meow()  # as you can see, we have unique method .meow and all other methods from animal

    dog.routine()

    cat.eat()
    dog.eat()

    # 02) super()

    square: Square = Square(20)
    square.describe()
    square.shape_method()
    rectangle: Rectangle = Rectangle(10, 15)
    rectangle.describe()
    rectangle.shape_method()


if __name__ == "__main__":
    main()
