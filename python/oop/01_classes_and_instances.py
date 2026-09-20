# Object Oriented Programming

# 01) Classes and Objects

# A class is a blueprint that contains all the information of an object
class Car:
    def __init__(self, brand: str, wheels: int) -> None:  # Initializer
        # Every time when we want to create a car we must provide info about brand and wheels
        self.brand = brand
        self.wheels = wheels

    def turn_on(self) -> None:  # we define some functionality for the car
        print(f"Turning on: {self.brand}")

    def turn_off(self) -> None:  # we define some functionality for the car
        print(f"Turning off: {self.brand}")

    def drive(self, km: float) -> None:  # we define some functionality for the car
        print(f"Driving: {self.brand} for {km}km")

    def describe(self) -> None:  # we define some functionality for the car
        print(f"{self.brand} is a car with {self.wheels} wheels")


# Now we have the blueprint of a basic car, that has brand, wheels, some basic functionality


def first_example() -> None:
    # Create an instance / object here
    bmw: Car = Car("BMW", 4)  # Created a car here,provided info about brand,wheels
    # Now we can describe the methods, which we created earlier
    # All the provided info will be applied directly to the object "bmw."
    bmw.turn_on()
    bmw.drive(10)
    bmw.turn_off()
    bmw.describe()

    volvo: Car = Car("Volvo", 6)  # Let's create another car!
    volvo.turn_on()
    volvo.drive(30)
    volvo.turn_off()
    volvo.describe()


# 2) __init__()


class Connection:  # Create a class
    # "self" refers to the current Instance of this class
    #   # Provide class with __init__ (allows to customize a class)
    def __init__(self, connection_type: str, cost: float) -> None:  # always None
        print(f"{connection_type} connection established! (Cost: ${cost}/h)")
        self.connection_type = connection_type  # self => current Instance of the class
        self.cost = cost

    def close_connection(self) -> None:  # Create one method to our Connection class
        print(f"Closing {self.connection_type} connection...")


def second_example() -> None:
    # "internet:" is an object and also an Instance of the class "Connection"; ("Internet", 2)=args
    internet: Connection = Connection("Internet", 2)
    # Another object or Instance of Connection
    satellite: Connection = Connection("Satellite", 20)

    internet.close_connection()
    satellite.close_connection()


# 03) self

# "self" refers to the current instance of the class; in other words, every time you create a new object
# you want all of the data that you insert into that class to be associated with that instance of the class(and not the class itself)


class Fruit:
    def __init__(self, name: str, grams: float) -> None:
        self.name = name  # instance attributes
        self.grams = grams  # that take info and store it inside that instance

    def eat(self) -> None:
        print(f"Eating {self.grams}g of {self.name}")


def third_example() -> None:
    # Let's create a few instances of this fruit
    apple: Fruit = Fruit("Apple", 25)  # apple now is associated with apple instance
    print(apple.name)  # Apple
    apple.eat()

    banana: Fruit = Fruit("Banana", 10)
    print(banana.name)  # Banana
    banana.eat()
    # 'self' makes sure that "("Banana", 10)" stays only in banana instance


# 04) Attributes (Class & Instance)


def main() -> None:
    # first_example()
    # second_example()
    third_example()


if __name__ == "__main__":
    main()
