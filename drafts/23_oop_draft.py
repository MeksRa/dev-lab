class Weapon:
    def __init__(self, name: str, damage: int) -> None:
        self.name = name
        self.damage = damage

    def __str__(self) -> str:
        return f"{self.name} (Damage: {self.damage})"


class Player:
    def __init__(self, name: str, hp: int, weapon: Weapon | None = None) -> None:
        self.name = name
        self.hp = hp
        self.weapon: Weapon | None = None

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
        self.hp = max(self.hp, 0)

    def is_alive(self) -> bool:
        return self.hp > 0

    def equip_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        print(f"🗡️  {self.name} equips {weapon.name}!")

    def attack(self, target: "Player") -> None:
        damage = self.weapon.damage if self.weapon else 5
        weapon_name = self.weapon.name if self.weapon else "fists"
        print(
            f"⚔️  {self.name} attacks {target.name}, using {weapon_name} deals {damage} damage!"
        )
        target.take_damage(damage)

    def __str__(self) -> str:
        status = f"❤️ {self.hp} HP" if self.is_alive() else "💀 Dead"
        weapon_info = (
            f" | Weapon: {self.weapon.name}" if self.weapon else " | No weapon"
        )
        return f"Player {self.name} [{status}]{weapon_info}"


def main() -> None:
    sword: Weapon = Weapon("Sword", 50)
    war: Player = Player("Good War", 200)
    sword2: Weapon = Weapon("Wooden Sword", 10)
    war2: Player = Player("Bad War", 110)

    # =========================================

    print("-" * 40)
    war.equip_weapon(sword)
    war2.equip_weapon(sword2)
    print("-" * 40)

    print(war)
    print(war2)
    print("-" * 40)

    # =========================================

    war.attack(war2)
    print(war2)
    print("-" * 40)

    war2.attack(war)
    print(war)

    # =========================================


if __name__ == "__main__":
    main()

# Output:
#
# ----------------------------------------
# 🗡️  Good War equips Sword!
# 🗡️  Bad War equips Wooden Sword!
# ----------------------------------------
# Player Good War [❤️ 200 HP] | Weapon: Sword
# Player Bad War [❤️ 110 HP] | Weapon: Wooden Sword
# ----------------------------------------
# ⚔️  Good War attacks Bad War, using Sword deals 50 damage!
# Player Bad War [❤️ 60 HP] | Weapon: Wooden Sword
# ----------------------------------------
# ⚔️  Bad War attacks Good War, using Wooden Sword deals 10 damage!
# Player Good War [❤️ 190 HP] | Weapon: Sword
#
