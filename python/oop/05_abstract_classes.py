# abstract classes
# are used as blueprints for other classes
# makes sure that the classes that are inheriting from another class actually follow the parent class structure

from abc import ABC, abstractmethod


class Appliance(ABC):  # inherits from ABC
    def __init__(self, brand: str, version_no: int) -> None:
        self.brand = brand
        self.version_no = version_no
        self.is_turned_on: bool = False

    @abstractmethod
    def turn_on(self) -> None: ...

    @abstractmethod
    def turn_off(self) -> None: ...


class Lamp(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)

    # u must implement this method, cuz of the decorator @abstractmethod
    def turn_on(self) -> None:
        if self.is_turned_on:
            print(f"{self.brand} is already turned on!")
        else:
            self.is_turned_on = True
            print(f"{self.brand} is now turned on!")

    # u must implement this method, cuz of the decorator @abstractmethod
    def turn_off(self) -> None:
        if self.is_turned_on:
            self.is_turned_on = False
            print(f"{self.brand} is now turned off!")
        else:
            print(f"{self.brand} is already turned off!")


# second example ====


class Oven(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)

    # u can't even run a program without these 2 methods, cuz u used @abstractmethod
    def turn_on(self) -> None:
        # good practice to use this line instead of "pass/..."
        raise NotImplementedError("Need to add functionality for turn_on()")

    def turn_off(self) -> None:
        # good practice to use this line instead of "pass/..."
        raise NotImplementedError("Need to add functionality for turn_on()")


def main() -> None:
    lamp: Lamp = Lamp("Z-Lite", 1)
    lamp.turn_on()
    lamp.turn_on()
    lamp.turn_off()
    lamp.turn_off()
    lamp.turn_on()
    lamp.turn_off()

    # ===== second example

    oven: Oven = Oven("Bosch", 2)
    oven.turn_on()  # it causes a NotImplementedError, cuz you haven't implement functionality yet
    oven.turn_off()  # it causes a NotImplementedError, cuz you haven't implement functionality yet


if __name__ == "__main__":
    main()
