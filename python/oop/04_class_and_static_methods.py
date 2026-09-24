from typing import Self  # for 02) @classmethod

# 01) @staticmethod ===================


class Calculator:
    def __init__(self, version: int) -> None:
        self.version = version

    @staticmethod  # transforms method into an isolated function inside the class
    def add(*numbers: float) -> float:
        return sum(numbers)

    def get_version(self) -> int:
        return self.version


# 02) @classmethod ===================
class Car:
    LIMITER: int = 200

    def __init__(self, brand: str, max_speed: int) -> None:
        self.brand = brand
        self.max_speed = max_speed

    @classmethod  # allows to modify "blueprint" for all objects
    def change_limit(cls, new_limit: int) -> None:  # "cls" means all objects,not "self"
        cls.LIMITER = new_limit

    @classmethod  # second example of using @classmethod
    def autogenerate_max_speed(cls, brand: str) -> Self:
        lowered: str = brand.lower()
        max_speed: int = 200
        if lowered == "toyota":
            max_speed = 270
        elif lowered == "bmw":
            max_speed = 290
        elif lowered == "volvo":
            max_speed = 300

        return cls(brand, max_speed)

    def display_info(self) -> None:
        print(f"{self.brand} (max={self.max_speed}, limiter={self.LIMITER})")


def main() -> None:
    # 01) @staticmethod ===================
    # @staticmethod allows to use class method directly without creating an instance
    result_wo_instances = Calculator.add(1, 2, 3, 4)
    print(f"({result_wo_instances}) result without instances")  # 10

    calc: Calculator = Calculator(version=1)
    result: float = calc.add(1, 2, 3, 4)
    print(f"({result}) result with instance")  # 10
    print(calc.get_version())  # 1

    # 02) @classmethod ===================

    bmw: Car = Car("BMW", 240)
    toyota: Car = Car("Toyota", 190)

    bmw.display_info()
    toyota.display_info()

    Car.change_limit(150)  # @classmethod changes LIMITER for each object here

    bmw: Car = Car("BMW", 240)
    toyota: Car = Car("Toyota", 190)

    # 03) #classmethod ===
    volvo: Car = Car.autogenerate_max_speed("Volvo")
    volvo.display_info()


if __name__ == "__main__":
    main()
