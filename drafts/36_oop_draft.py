import random
import time


class Item:
    def __init__(self, name: str, heal: int) -> None:
        self.name = name
        self.heal = heal

    def __repr__(self) -> str:
        return f"{self.name} (+{self.heal} HP)"


class Inventory:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def has_items(self) -> bool:
        return len(self.items) > 0

    def pop_item(self) -> Item | None:
        if self.has_items():
            return self.items.pop(0)
        return None


# ---


class Character:
    def __init__(self, name: str, health: int, attack_power: int) -> None:
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.inventory = Inventory()

    def is_alive(self) -> bool:
        return self.health > 0

    def attack(self, target: "Character") -> None:
        damage = max(1, self.attack_power + random.randint(-3, 3))  # +- 3 damage
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        self.health = max(self.health, 0)
        print(f"{self.name} has {self.health}/{self.max_health} HP left")

    def use_item(self) -> bool:
        """Tries to use an item from inventory, returns TRUE if an item was used."""
        if not self.inventory.has_items():
            return False

        item = self.inventory.pop_item()
        if item:
            old_hp = self.health
            self.health = min(self.max_health, self.health + item.heal)
            healed = self.health - old_hp
            print(
                f"{self.name} uses {item.name} and heals {healed} HP! (Now has {self.health}/{self.max_health} HP)"
            )
            return True
        return False


# ---


def start_battle(player1: Character, player2: Character) -> None:
    print("=" * 40)
    print(f"FIGHT: {player1.name} VS {player2.name}")
    print("=" * 40)

    round_num = 1
    fighters = [player1, player2]

    while player1.is_alive() and player2.is_alive():
        print(f"\n--- -- Round {round_num} -- ---")

        # shuffle turn order
        attacker, defender = fighters[0], fighters[1]

        # warrior logic
        # if hp < 40% and has a potion -> drink, else attack
        if (
            attacker.health < (attacker.max_health * 0.4)
            and attacker.inventory.has_items()
        ):
            attacker.use_item()
        else:
            attacker.attack(defender)

        if not defender.is_alive():
            print(f"\n{defender.name} is dead!")
            print(f"{attacker.name} win!")
            break

        # swap roles
        fighters.reverse()
        round_num += 1
        time.sleep(0.8)  # pause simulation


def main() -> None:
    dog = Character(name="Dog", health=100, attack_power=18)
    cat = Character(name="Cat", health=80, attack_power=22)
    potions_pool = [
        Item("Small HP potion", 25),
        Item("Medium HP potion", 35),
        Item("Big HP potion", 45),
        Item("Super Elixir", 60),
    ]
    total_potions_count = 10  # Potions amount

    prepared_potions = [random.choice(potions_pool) for _ in range(total_potions_count)]
    for item in prepared_potions:
        # random.choice is making a choice: dog or cat
        receiver = random.choice([dog, cat])
        receiver.inventory.add_item(item)
    print(
        f"Inv: {dog.name}({len(dog.inventory.items)}):\n"
        + "\n".join(f"   - {item}" for item in dog.inventory.items)
    )
    print(
        f"Inv: {cat.name}({len(cat.inventory.items)}):\n"
        + "\n".join(f"   - {item}" for item in cat.inventory.items)
    )

    start_battle(dog, cat)


if __name__ == "__main__":
    main()
