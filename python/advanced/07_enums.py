from enum import Enum

# enum - enumerate, if you have fixed set of options:
# (status, roles, days of the week, operating modes, so on..)
# but u should choose only one. Enum Creates new types, e.g. "State"/ "Color / "ROLE".
# (NEW/IN_PROGRESS/DONE) / (ADMIN/USER/GUEST) / (ON/OFF)
# and if you wanna protect ur code from random mistakes, magic numbers etc - use enum


class State(Enum):
    OFF = 0
    ON = 1


state: State = State.OFF

if state == State.ON:
    print("The device is turned on.")
elif state == State.OFF:
    print("Device is turned off.")
else:
    print("Unknown input...")

# ----


class Color(Enum):
    RED = "R"
    GREEN = "G"
    BLUE = "B"


red: Color = Color.RED
print(red)         # Color.RED
print(red.value)   # R
print(red.name)    # RED
print(Color("R"))  # Color.RED

# ----


def buy_car(brand: str, color: Color) -> None:
    if color == Color.RED:
        print(f"You bought a smoking hot red {brand}!")
    elif color == Color.GREEN:
        print(f"You bought a chill green {brand}!")
    elif color == Color.BLUE:
        print(f"You bought a smooth blue {brand}!")
    else:
        print("Unknown color.")


def main() -> None:
    buy_car("BMW", Color.BLUE)      # You bought a smooth blue BMW!
    buy_car("Volvo", Color.RED)     # You bought a smoking hot red Volvo!
    buy_car("Toyota", Color.GREEN)  # You bought a chill green Toyota!
    buy_car("Mercedes", Color.RED)  # You bought a smoking hot red Mercedes!


if __name__ == "__main__":
    main()
