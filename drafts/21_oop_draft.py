class Hero:
    def __init__(self, name: str, weapon: "Weapon", armor: "Armor") -> None:
        # character data
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.gold = 50
        # stats
        self.base_attack = 10
        # equip
        self.weapon = weapon
        self.armor = armor
        # inventory
        self.inventory = Inventory(max_slots=5)

    # Battle Logic
    def attack(self, target_name: str) -> int:
        return self.base_attack + self.weapon.get_effective_damage()

    def take_damage(self, damage: int) -> int:
        actual_damage = max(1, damage - self.armor.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def is_alive(self) -> bool:
        return self.hp > 0

    def heal(self, amount: int) -> int:
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        return self.hp - old_hp

    # Inventory and shop logic

    def buy_item(self, item_name: str, price: int) -> bool:
        if self.gold < price:
            return False
        if self.inventory.add_item(item_name):
            self.gold -= price
            return True
        return False


class HeroUI:
    @staticmethod
    def print_stats(hero: Hero) -> None:
        """Gets object Hero and prints it into console."""
        total_attack = hero.base_attack + hero.weapon.get_effective_damage()

        print("\n" + "=" * 30)
        print(f"   Characteristics: {hero.name} (Ур. {hero.level})")
        print("=" * 30)
        print(f"❤️  HP: {hero.hp}/{hero.max_hp}")
        print(f"🗡️  Damage: {total_attack} ({hero.weapon.name})")
        print(f"🛡️️  Block: {hero.armor.defense} ({hero.armor.name})")
        print(f"💰 Gold: {hero.gold}")

        items_str = ", ".join(hero.inventory.items) if hero.inventory.items else "Empty"
        print(
            f"🎒 Inventory ({len(hero.inventory.items)}/{hero.inventory.max_slots}): {items_str}"
        )
        print("=" * 30 + "\n")


class Weapon:
    def __init__(self, name: str, damage: int, durability: int = 100) -> None:
        self.name = name
        self.damage = damage
        self.durability = durability

    def get_effective_damage(self) -> int:
        """If the weapon is broken(durability==0) => Weapon Damage = 0."""
        if self.durability <= 0:
            return 0
        return self.damage


class Armor:
    def __init__(self, name: str, defense: int) -> None:
        self.name = name
        self.defense = defense


class Inventory:
    def __init__(self, max_slots: int = 5) -> None:
        self.items: list[str] = []
        self.max_slots = max_slots

    def add_item(self, item_name: str) -> bool:
        """add item if you have free space"""
        if len(self.items) < self.max_slots:
            self.items.append(item_name)
            print(f"🎒 item '{item_name}' added to the inventory!")
            return True
        print(f"❌ Inventory is full! Can't grab '{item_name}'")
        return False

    def remove_item(self, item_name: str) -> bool:
        """remove item if it's there"""
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"🗑️ Item '{item_name}' has been removed!")
            return True
        print(f"❌ Item '{item_name}' not in the inventory!")
        return False

    def is_full(self) -> bool:
        return len(self.items) >= self.max_slots


if __name__ == "__main__":
    iron_sword = Weapon(name="Iron Sword", damage=5)
    leather_armor = Armor(name="Leather Armor", defense=4)
    hero = Hero("MeksRa", weapon=iron_sword, armor=leather_armor)

    hero.inventory.add_item("hp potion lvl 2")

    HeroUI.print_stats(hero)

    hero.inventory.add_item("strength potion lvl 4")
    hero.inventory.add_item("apple")
    hero.inventory.add_item("apple")
    hero.inventory.add_item("apple")
    hero.inventory.add_item("apple")

    damage_dealt = hero.attack("Goblin")
    print(f"⚔️ {hero.name} dealt {damage_dealt} damage to Goblin!")
    magic_staff = Weapon(name="Staff of Fire", damage=25)
    hero.weapon = magic_staff
    damage_dealt = hero.attack("Goblin")
    print(f"⚔️ {hero.name} dealt {damage_dealt} damage to Goblin!")
    taken_damage = hero.take_damage(20)
    print(f"🛡️ {hero.name} took {taken_damage} damage. Remaining HP: {hero.hp}")

    HeroUI.print_stats(hero)

# Output:
# ==============================
# ❤️  HP: 100/100
# 🗡️  Damage: 15 (Iron Sword)
# 🛡️️  Block: 4 (Leather Armor)
# 💰 Gold: 50
# 🎒 Inventory (1/5): hp potion lvl 2
# ==============================
#
# 🎒 item 'strength potion lvl 4' added to the inventory!
# 🎒 item 'apple' added to the inventory!
# 🎒 item 'apple' added to the inventory!
# 🎒 item 'apple' added to the inventory!
# ❌ Inventory is full! Can't grab 'apple'
# ⚔️ MeksRa dealt 15 damage to Goblin!
# ⚔️ MeksRa dealt 35 damage to Goblin!
# 🛡️ MeksRa took 16 damage. Remaining HP: 84
#
# ==============================
#    Characteristics: MeksRa (Ур. 1)
# ==============================
# ❤️  HP: 84/100
# 🗡️  Damage: 35 (Staff of Fire)
# 🛡️️  Block: 4 (Leather Armor)
# 💰 Gold: 50
# 🎒 Inventory (5/5): hp potion lvl 2, strength potion lvl 4, apple, apple, apple
# ==============================
