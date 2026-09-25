class HeroInventory:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.items: list[str] = []
    def add_item(self, item_name: str) -> bool:
        if len(self.items) < self.capacity:
            self.items.append(item_name)
            return True
        return False

    def remove_item(self, item_name: str) -> bool:
        if item_name in self.items:
            self.items.remove(item_name)
            return True
        return False
    def get_items_count(self) -> int:
        return len(self.items)

def main() -> None:
    inv = HeroInventory(capacity=2)

    print(inv.add_item("Health Potion")) # True
    print(inv.add_item("Mana Potion")) # True
    print(inv.add_item("Sword"))  # False

    print(inv.get_items_count()) # 2

    print(inv.remove_item("Health Potion")) # True
    print(inv.remove_item("Shield")) # False

    print(inv.get_items_count()) # 1



if __name__ == "__main__":
    main()