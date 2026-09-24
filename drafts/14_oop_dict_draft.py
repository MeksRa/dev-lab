class Inventory:
    def __init__(self) -> None:
        self.__items: dict = {}

    def add_item(self, sku: str, name: str, price: float, quantity: int) -> None:
        if sku in self.__items:
            self.__items[sku]["quantity"] += quantity
            print(
                f'Quantity of item "{name}" updated: {self.__items[sku]["quantity"]} pcs.'
            )
        else:
            self.__items[sku] = {"name": name, "price": price, "quantity": quantity}
            print(f'Item "{name}" successfully added!')

    def get_item(self, sku: str) -> dict | None:
        return self.__items.get(sku)

    def remove_item(self, sku: str) -> bool:
        if sku in self.__items:
            del self.__items[sku]
            return True
        return False

    def get_total_value(self) -> float:
        total = 0.0
        for item in self.__items.values():
            total += item["price"] * item["quantity"]
        return total

    def show_items(self) -> None:
        if not self.__items:  # Guard Clause
            print("Warehouse is empty")
            return  # 1

        print("\n--- List of items in stock ---")
        for sku, item in self.__items.items():
            print(
                f"[{sku}] {item['name']} | Price: ${item['price']} | Quantity: {item['quantity']} pcs."
            )

    def __str__(self) -> str:
        return f"Warehouse: items - {len(self.__items)}, total value - ${self.get_total_value():.2f}"


def main() -> None:
    inv: Inventory = Inventory()
    print(inv)
    inv.add_item("TV_MODEL_3000", "TV", 150.0, 5)
    inv.add_item("SAMSUNG", "Smartphone", 90.0, 4)
    print(inv)
    inv.show_items()
    print(inv._Inventory__items)


if __name__ == "__main__":
    main()
