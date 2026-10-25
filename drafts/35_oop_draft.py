class Item:
    def __init__(self, name: str, slots: int = 1) -> None:
        self.name = name
        self.slots = slots

    def __str__(self) -> str:
        return f"{self.name} (Slots: {self.slots})"


class Potion(Item): ...
class Weapon(Item): ...

class Armor(Item): ...

class Helmet(Armor):
    def __init__(self, name):
        super().__init__(name, slots = 2)
class Trousers(Armor):
    def __init__(self, name):
        super().__init__(name, slots = 4)
class BreastPlate(Armor):
    def __init__(self, name):
        super().__init__(name, slots = 5)
class Shoes(Armor):
    def __init__(self, name):
        super().__init__(name, slots = 2)


class Inventory:
    def __init__(self, max_slots: int = 10) -> None:
        self.max_slots = max_slots
        self.items: list[Item] = []

    def add_item(self, item: Item) -> str:
        
        current_used_slots = sum(i.slots for i in self.items)
        
        if current_used_slots + item.slots > self.max_slots:
            return "Not enough slots in inventory."



        self.items.append(item)
        return f"{item} added to inventory."

    def remove_item(self, item: Item) -> str:
        if not item in self.items:
            return "Item not found"

        self.items.remove(item)
        return f"{item} removed from inventory."

    def show_items(self) -> str:
        if not self.items:
            return "Inventory is empty!"

        items_list_str = "\n".join(f"- {item}" for item in self.items)
        return f"Items in inventory:\n{items_list_str}"

    def __str__(self) -> str:
        used_slots = sum(i.slots for i in self.items)
        return f"Inventory: {used_slots}/{self.max_slots} slots used"


# ---
def main() -> None:
    inv: Inventory = Inventory()


if __name__ == "__main__":
    main()
