class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

    def turn_on(self) -> str:
        if self.turned_on:
            return f'"{self.brand}" is already turned on!'
        self.turned_on = True
        return f'"{self.brand}" is turned on!'

    def turn_off(self) -> str:
        if not self.turned_on:
            return f'"{self.brand}" is already turned off!'
        self.turned_on = False
        return f'"{self.brand}" is turned off!'

    def run(self, seconds: int) -> str:
        if self.turned_on:
            return f'Running "{self.brand}" for "{seconds} seconds'
        return "Turn on your Microwave first!"

    def __str__(self) -> str:
        return f'Microwave "{self.brand}" has power rating "{self.power_rating}"'

    def __repr__(self) -> str:
        return (
            f'REPR: Microwave(brand="{self.brand}", power_rating="{self.power_rating}")'
        )

    def __add__(self, other: "Microwave") -> str:
        return f"{self.brand} + {other.brand} = microwaves"


def main() -> None:
    bosch: Microwave = Microwave("Bosch", "A")
    lg: Microwave = Microwave("LG", "B")
    samsung: Microwave = Microwave("Samsung", "C")
    print(bosch)
    print(repr(bosch))
    print(lg.run(10))
    print(lg.turn_off())
    print(lg.turn_on())
    print(lg.run(10))
    print(samsung + lg)


if __name__ == "__main__":
    main()
