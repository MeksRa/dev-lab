# 01) Dunder Methods / Magic Methods
# We never call them directly

from typing import Self


class Book:
    def __init__(self, title: str, pages: int) -> None:  # Initializer
        self.title = title
        self.pages = pages

    def __len__(self) -> int:  # built-in length function
        return self.pages

    def __add__(self, other: Self) -> "Book":
        combined_title: str = f"{self.title} & {other.title}"
        combined_pages: int = self.pages + other.pages
        return Book(combined_title, combined_pages)


def first_example() -> None:
    py_daily: Book = Book("PyDaily", 100)
    harry_potter: Book = Book("Harry Potter", 340)
    print(len(py_daily))  # use this func to get the length
    print(len(harry_potter))

    #  py_daily.__len__() # => bad practice to use it this way

    combined_books: Book = py_daily + harry_potter
    print(combined_books.title)
    print(combined_books.pages)


# 02) __str__() & __repr__()


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:  # easy to read for user/yourself
        return f"{self.name}: {self.age} years old"

    def __repr__(self) -> str:  # more useful for technical use
        return f"Person(name={self.name}, age={self.age})"


def second_example() -> None:
    mario: Person = Person("Mario", 27)
    # with repr() or without it, without __str__, __repr__ we will get result show below:
    print(repr(mario))  # <__main__.Person object at 0x000001A131C68C20>
    print(repr(mario))  # Person(name=Mario, age=27)  # (with __repr__)
    print(mario)  # Mario: 27 years old # (with __str__)


# 03) __eq__()


class Car:
    def __init__(self, brand: str, car_id: int, colour: str) -> None:
        self.brand = brand
        self.car_id = car_id
        self.colour = colour

    def __eq__(self, other: object) -> bool:
        # return self.car_id == other.car_id  # => that's enough to get "True"
        print("Current:", self.__dict__)
        print("Other:", other.__dict__)
        return self.__dict__ == other.__dict__


def third_example() -> None:
    car1: Car = Car("BMW", 1, "red")
    car2: Car = Car("BMW", 1, "red")
    # We ask here if they the same object
    print(car1 == car2)  # False # => they both have different memory adresses
    print(car1, car2)
    # <__main__.Car object at 0x000001F2967F8AD0> <__main__.Car object at 0x000001F2967E8910>

    # but after we added __eq__, we changed the result:

    # Current: {'brand': 'BMW', 'car_id': 1, 'colour': 'red'}
    # Other: {'brand': 'BMW', 'car_id': 1, 'colour': 'red'}
    # True


# 04) Difference between a method and a function in Python


class Connection:
    def __init__(self, connection_type: str) -> None:  # Dunder method
        self.connection_type = connection_type

    def connect(self) -> None:  # Regular method
        # (any function that defined inside the class)
        print(f"Connecting to: {self.connection_type}")


def fourth_example():
    def connect(connection_type: str) -> None:  # Function
        # (defined outside of the class)
        print(f"Connecting to: {connection_type}")


def main():
    # first_example()
    # second_example()
    # third_example()
    fourth_example()


if __name__ == "__main__":
    main()
