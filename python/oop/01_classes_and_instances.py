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
    apple.eat()  # Eating 25g of Apple

    banana: Fruit = Fruit("Banana", 10)
    print(banana.name)  # Banana
    banana.eat()  # Eating 10g of Banana
    # 'self' makes sure that "("Banana", 10)" stays only in banana instance


# 04) Attributes (Class & Instance)
# With self we can define instance attributes which are any attributes that belongs to the class

# All the variables and functions inside the class are named as attributes.
# Instance attributes => self.name ; Class attributes => general variables for each object of the class
# function inside a class is a method.
# first argument is 'self', serves as a link to object.

# Usually we use Class attributes to tell python that this info should be shared amongs all the instances(not the classes)


class Vehicle:
    SPEED_LIMIT_KM: float = 140  # Class Attribute (shares amongs all the instances)

    def __init__(self, brand: str) -> None:  # define instance atr inside initializer
        self.brand = brand  # Instance Attribute

    def drive(self, *, speed: float) -> None:  # define a drive method;
        # "*" means "require" key arg
        if speed > self.SPEED_LIMIT_KM:
            print(f"Limiter activated: Driving at {self.SPEED_LIMIT_KM}km/h")
        else:
            print(f"Driving at {speed}km/h")


def fourth_example():
    toyota: Vehicle = Vehicle("Toyota")
    bmw: Vehicle = Vehicle("Toyota")

    toyota.drive(speed=200)
    bmw.drive(speed=210)

    Vehicle.SPEED_LIMIT_KM = 99  # each instance will reach the limit
    # toyota.SPEED_LIMIT_KM = 99 # => only toyota will reach the speed limit
    toyota.drive(speed=200)
    bmw.drive(speed=210)


class Animal:
    # tricks: list[str] = []  # => bad practice to use it like a class attribute here

    def __init__(self, name) -> None:
        self.name = name
        self.tricks: list[str] = []

    def teach_trick(self, trick_name: str) -> None:
        self.tricks.append(trick_name)


def fifth_example():
    cat: Animal = Animal("Helios")
    dog: Animal = Animal("Boomer")

    cat.teach_trick("Wash dishes")
    cat.teach_trick("Get a job")
    print(cat.tricks)

    dog.teach_trick("Do finances")
    dog.teach_trick("Invest in stocks")
    print(dog.tricks)


# Class => class Car => Blueprint/Template
# Instance / Object => my_car = Car() => an object created from a blueprint
# self => self.brand => Pointer to "Me" (to a specific object)
# Class Attribute => SPEED_LIMIT = 140 => Constant / Setting common to the entire plant
# Instance Attribute => self.color = "Red" => Personal characterization of a specific object


def main() -> None:
    # first_example()
    # second_example()
    # third_example()
    # fourth_example()
    fifth_example()


if __name__ == "__main__":
    main()
