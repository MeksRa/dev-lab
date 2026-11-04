from dataclasses import dataclass


@dataclass
class Coffee:
    name: str
    ingredients: dict[str, int]
    price: float


class Storage:
    """Storage facility for coffee machine ingredients."""

    def __init__(self, initial_resourses: dict[str, int]) -> None:
        self.items = initial_resourses

    def add(self, item: str, amount: int) -> None:
        """Replenishes the supply of a specific ingredient."""
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

    def check_availability(self, required: dict[str, int]) -> bool:
        """Checks whether all the ingredients required for a recipe are available in stock."""
        for item, needed_amount in required.items():
            if self.items.get(item, 0) < needed_amount:
                return False
        return True

    def consume(self, required: dict[str, int]) -> None:
        """Deducts ingredients from inventory when preparing coffee."""
        for item, needed_amount in required.items():
            if item in self.items:
                self.items[item] -= needed_amount

    def __str__(self) -> str:
        lines = ["Ingredients storage"]
        for item, amount in self.items.items():
            lines.append(f"- {item}: {amount}")
        return "\n".join(lines)


class CoffeeMachine:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage
        self.money: float = 0.0
        self.menu: list[Coffee] = []

    def add_recipe(self, coffee: Coffee) -> None:
        self.menu.append(coffee)

    def show_menu(self) -> str:
        if not self.menu:
            return "Menu is empty"
        lines = ["Menu:"]
        for i, coffee in enumerate(self.menu, start=1):
            lines.append(f"{i}. {coffee.name} - ${coffee.price}")
        return "\n".join(lines)

    def make_coffee(self, choice_index: int, inserted_money: float) -> str:
        index = choice_index - 1
        if not (0 <= index < len(self.menu)):
            return "Error. There is no such drink."
        coffee = self.menu[index]

        # Checking if there is enough money
        if inserted_money < coffee.price:
            return f"Not enough money. {coffee.name} costs ${coffee.price}."

        # Checking the warehouse to see if there are enough ingredients.
        if not self.storage.check_availability(coffee.ingredients):
            return f"Not enough ingredients for '{coffee.name}'!"

        # Deducting ingredients from the storage
        self.storage.consume(coffee.ingredients)

        # Accepting payment and provide change
        self.money += coffee.price
        change = inserted_money - coffee.price
        change_text = (
            f"Inserted: {inserted_money}. Price: {coffee.price}. (Change: ${change})"
            if change > 0
            else ""
        )
        return f"Coffee {coffee.name} is being prepared! Enjoy! {change_text}"


def main() -> None:
    my_storage = Storage({"water": 1000, "beans": 200, "milk": 500})
    machine = CoffeeMachine(my_storage)
    # ---

    espresso = Coffee("Espresso", {"water": 50, "beans": 15}, price=150.0)
    cappuccino = Coffee(
        "Cappuccino", {"water": 50, "beans": 15, "milk": 100}, price=220.0
    )
    # ---

    machine.add_recipe(espresso)
    machine.add_recipe(cappuccino)

    print(machine.show_menu())
    print("-" * 20)
    print(machine.storage)
    print("-" * 20)

    print(machine.make_coffee(2, inserted_money=250.0))
    print("-" * 20)
    print(machine.storage)


if __name__ == "__main__":
    main()

# OUTPUT
# Menu:
# 1. Espresso - $150.0
# 2. Cappuccino - $220.0
# --------------------
# Ingredients storage
# - water: 1000
# - beans: 200
# - milk: 500
# --------------------
# Coffee Cappuccino is being prepared! Enjoy! Inserted: 250.0. Price: 220.0. (Change: $30.0)
# --------------------
# Ingredients storage
# - water: 950
# - beans: 185
# - milk: 400
