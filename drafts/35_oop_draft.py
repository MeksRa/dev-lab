class Item:
    def __init__(self, name: str, slots: int = 1) -> None:
        self.name = name
        self.slots = slots

    def __str__(self) -> str:
        return f"{self.name} (Slots: {self.slots})"


class Potion(Item): ...

class HealthPotion(Potion):
    def __init__(self, name: str, heal: int) -> None:
        super().__init__(name)
        self.heal = heal

    def __str__(self) -> str:
        base_str = super().__str__()[:-1]
        return f"{base_str}, Heal: {self.heal})"
    
class StrengthPotion(Potion):
    def __init__(self, name: str, strength_bonus: int) -> None:
        super().__init__(name)
        self.strength_bonus = strength_bonus

    def __str__(self) -> str:
        base_str = super().__str__()[:-1]
        return f"{base_str}, Strength: {self.strength_bonus})"




class Weapon(Item): ...

class OneHanded(Weapon): ...
class TwoHanded(Weapon): ...

class Armor(Item):
    def __init__(self, name: str, slots: int, protection: int) -> None:
        super().__init__(name, slots)
        self.protection = protection

    def __str__(self) -> str:
        return f"{self.name} (Slots: {self.slots}, Protection: {self.protection})"
    
class Helmet(Armor):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name, slots = 2, protection = protection)
class Trousers(Armor):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name, slots = 4, protection = protection)
class BreastPlate(Armor):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name, slots = 5, protection = protection)
class Shoes(Armor):
    def __init__(self, name: str, protection: int) -> None:
        super().__init__(name, slots = 2, protection = protection)


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
    # ---
    dragon_helmet = Helmet("Dragon helmet", 30)
    dragon_trousers = Trousers("Dragon trousers", 60)
    dragon_shoes = Shoes("Dragon Shoes", 25)
    dragon_breastplate = BreastPlate("Dragon breastplate", 80)
    # ---
    leather_helmet = Helmet("leather helmet", 15)
    leather_trousers = Trousers("leather trousers", 30)
    leather_shoes = Shoes("leather Shoes", 12)
    leather_breastplate = BreastPlate("leather breastplate", 40)
    # ---
    big_health_potion = HealthPotion("Big Health Potion", 200)
    health_potion = HealthPotion("Health Potion", 100)
    big_strength_potion = StrengthPotion("Big Strength Potion", 200)
    strength_potion = StrengthPotion("Strength Potion", 100)
    # ---

if __name__ == "__main__":
    main()
