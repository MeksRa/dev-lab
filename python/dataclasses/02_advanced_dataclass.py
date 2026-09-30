# ==========
# __post_init__  # post initilizer
# ==========
# ==========
# InitVar
# ==========
from dataclasses import InitVar, dataclass, field


@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    is_rare: InitVar[bool | None] = None  # InitVar  # Only for initializing Fruit
    total_price: float = field(init=False)

    def __post_init__(self, is_rare: bool | None) -> None:
        # code that will happen after original __init__
        # only once and can't be changed in future

        if is_rare:
            self.price_per_kg *= 2

        self.total_price = (self.grams / 1000) * self.price_per_kg

    def describe(self) -> None:
        print(f"{self.grams}g of {self.name} costs ${self.total_price}")


# ==========
# @property
# ==========
@dataclass
class FruitSecondExample:
    name: str
    grams: float
    price_per_kg: float

    @property
    def total_price(self) -> float:
        return (self.grams / 1000) * self.price_per_kg

    def describe(self) -> None:
        print(f"{self.grams}g of {self.name} costs ${self.total_price}")


def main() -> None:
    # ====================

    apple: Fruit = Fruit("Apple", 1500, 5)
    orange: Fruit = Fruit("Apple", 2500, 10)
    print(apple)
    # Fruit(name='Apple', grams=1500, price_per_kg=5, total_price=7.5)
    print(orange)
    # Fruit(name='Apple', grams=2500, price_per_kg=10, total_price=25.0)
    apple.describe()  # 1500g of Apple costs $7.5
    orange.describe()  # 2500g of Apple costs $25.0

    # ====================
    passion: Fruit = Fruit("Passion", 100, 50, is_rare=True)
    passion.describe()  # 100g of Passion costs $10.0
    print(passion)
    # Fruit(name='Passion', grams=100, price_per_kg=100, total_price=10.0)
    # ====================
    print(apple)
    # FruitSecondExample(name='Apple2', grams=1500, price_per_kg=5)
    apple.describe()  # 1500g of Apple costs $7.5
    apple.price_per_kg = 20
    print(apple)
    # FruitSecondExample(name='Apple2', grams=1500, price_per_kg=20)
    apple.describe()  # 1500g of Apple costs $7.5  # => Nothing updated
    # the reason is postinit

    apple2: FruitSecondExample = FruitSecondExample("Apple2", 1500, 5)
    print(apple2)
    # FruitSecondExample(name='Apple2', grams=1500, price_per_kg=5)
    apple.describe()  # 1500g of Apple costs $7.5
    apple2.price_per_kg = 20
    print(apple2)
    # FruitSecondExample(name='Apple2', grams=1500, price_per_kg=20)
    apple2.describe()  # 1500g of Apple2 costs $30.0  # => Updated


if __name__ == "__main__":
    main()
