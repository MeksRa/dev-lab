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


def main() -> None:
    dog: Dog = Dog("Jack(dog)")
    cat: Cat = Cat("Destroyer of Worlds(cat)")

    dog.bark()  # as you can see, we have unique method .bark and all other methods from animal
    cat.meow()  # as you can see, we have unique method .meow and all other methods from animal

    dog.routine()

    cat.eat()
    dog.eat()


if __name__ == "__main__":
    main()
