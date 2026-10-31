class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

    def __str__(self) -> str:
        return f"{self.name} (Damage: {self.damage})"


class Inventory:
    def __init__(self, capacity: int = 5) -> None:
        self.capacity = capacity
        self.items: list[str] = []

    def add_item(self, item: str) -> None:
        if len(self.items) >= self.capacity:
            print("Inventory is full")
            return
        self.items.append(item)
        print(f"Item {item} added to the inventory")

    def __str__(self) -> str:
        return ",".join(self.items) if self.items else "Empty"


class Player:
    def __init__(self, name: str, weapon: Weapon) -> None:
        self.name = name
        self.weapon = weapon
        self.inventory = Inventory(capacity=5)

    def attack(self) -> None:
        print(
            f"{self.name} attacks enemy with {self.weapon.name} and deals {self.weapon.damage} damage!"
        )

    def pick_up(self, item: str) -> None:
        self.inventory.add_item(item)

    def show_status(self) -> None:
        print(f"-- --- Player: {self.name} --- --")
        print(f"Weapon: {self.weapon}")
        print(f"Inventory: {self.inventory}")


def main() -> None:
    rusty_sword = Weapon("Rusty Sword", 15)

    hero = Player("Stranger", weapon=rusty_sword)
    hero.show_status()

    print()
    hero.attack()
    print()

    hero.pick_up("HP potion")
    hero.pick_up("Dungeon key")

    print("!!!FOUND A NEW WEAPON!!!")
    hero.weapon = Weapon("Fire staff", 40)
    hero.show_status()


if __name__ == "__main__":
    main()
