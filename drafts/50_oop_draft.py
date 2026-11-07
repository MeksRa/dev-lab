from dataclasses import dataclass
from typing import Self


@dataclass
class Product:
    name: str
    _price: float  # for validation
    stock: int = 0

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Cannot be below zero")
        self._price = value

    @staticmethod
    def format_price(amount: float) -> str:
        return f"${amount:.2f}"

    @classmethod
    def create_with_discount(
        cls, name: str, base_price: float, discount_percent: float
    ) -> Self:
        final_price = base_price * (1 - discount_percent / 100)
        return cls(name=name, _price=final_price, stock=10)


class ShoppingCart:
    def __init__(self) -> None:
        self._items: list[Product] = []

    def add_item(self, product: Product) -> None:
        if product.stock > 0:
            self._items.append(product)
            print(f"'{product.name}' has been added")
        else:
            print(f"'{product.name}' has already been sold")

    def remove_item(self, product_name: str) -> None:
        self._items = [item for item in self._items if item.name != product_name]
        print(f"'{product_name}' has been removed")

    @property
    def total(self) -> float:
        return sum(item.price for item in self._items)

    @property
    def count(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        if not self._items:
            return "Empty"
        items_str = ", ".join(item.name for item in self._items)
        return f"[{self.count}] | {items_str} | Sum: {Product.format_price(self.total)}"


def main() -> None:
    item1 = Product("Keyboard", 120.0, stock=5)
    item2 = Product.create_with_discount("Mouse", base_price=80.0, discount_percent=20)

    cart = ShoppingCart()

    cart.add_item(item1)
    cart.add_item(item2)

    print("\n" + str(cart))
    print(f"Accurate sum through the getter cart.total: {cart.total}\n")

    cart.remove_item("Mouse")
    print(str(cart))


if __name__ == "__main__":
    main()

# OUTPUT:
# 'Keyboard' has been added
# 'Mouse' has been added

# [2] | Keyboard, Mouse | Sum: $184.00
# Accurate sum through the getter cart.total: 184.0

# 'Mouse' has been removed
# [1] | Keyboard | Sum: $120.00
