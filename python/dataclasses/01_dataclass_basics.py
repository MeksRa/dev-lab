# ==========
# @dataclass
# ==========
from dataclasses import dataclass, field


@dataclass
class Coin:
    name: str
    value: float
    id: str


# ==========
# Fields
# ==========


@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    edible: bool = field(default=True)  # or just => edible: bool = True
    related_fruits: list[str] = field(default_factory=list)


def main() -> None:
    bitcoin: Coin = Coin("Bitcoin", 10_000, "BTC")
    bitcoin2: Coin = Coin("Bitcoin", 10_000, "BTC")
    ripple: Coin = Coin("Ripple", 200, "XRP")

    print(bitcoin)  # Coin(name='Bitcoin', value=10000, id='BTC')
    print(ripple)  # Coin(name='Ripple', value=200, id='XRP')

    print(bitcoin.value == ripple.value)  # False
    print(bitcoin == ripple)  # False
    print(bitcoin == bitcoin2)  # True

    # =======================

    apple: Fruit = Fruit("Apple", 100, 5)
    pear: Fruit = Fruit("Pear", 250, 10, edible=False)  # or just <False>
    pineapple: Fruit = Fruit("Pineapple", 500, 15, related_fruits=["Apple", "Orange"])
    print(apple)
    # Fruit(name='Apple', grams=100, price_per_kg=5, edible=True, related_fruits=[])
    print(pear)
    # Fruit(name='Pear', grams=250, price_per_kg=10, edible=False, related_fruits=[])
    print(pineapple)
    # Fruit(name='Pineapple', grams=500, price_per_kg=15, edible=True, related_fruits=['Apple', 'Orange'])


if __name__ == "__main__":
    main()
