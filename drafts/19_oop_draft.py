from abc import ABC, abstractmethod


class NotEnoughManaError(Exception): ...


class Armor:
    def __init__(self, name: str, defense: int) -> None:
        self.name = name
        self.defense = defense

    def __str__(self) -> str:
        return f"{self.name} (Def: {self.defense})"


class Hero(ABC):
    total_heroes_count: int = 0

    def __init__(self, name: str, health: int, damage: int, level: int = 1) -> None:
        self.name = name
        self.damage = damage
        self._health = health  # protected
        self._level = level  # protected
        Hero.total_heroes_count += 1
        self.armor: Armor | None = None  # # Composition: Hero HAS-A Armor

    def __str__(self) -> str:
        armor_info = f", Armor: {self.armor.name}" if self.armor else ""
        return f"| {self.name} => Lvl: {self.level} | HP: {self.health} | DMG: {self.damage} | {armor_info}|"

    @classmethod
    def get_total_count(cls) -> int:
        return cls.total_heroes_count

    @property  # getter
    def health(self) -> int:
        return self._health

    @property
    def level(self) -> int:
        return self._level

    @health.setter  # setter
    def health(self, value: int) -> None:
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @level.setter
    def level(self, value: int) -> None:
        if value < 1:
            self._level = 1
        else:
            self._level = value

    def equip_armor(self, armor: Armor) -> None:
        self.armor = armor
        print(f"{self.name} equipped {armor.name}")

    def attack(self, target: "Hero") -> None:
        damage_dealt = target.take_damage(self.damage)
        print(
            f"{self.name} attacks {target.name} for {damage_dealt} damage! "
            f"({target.name} remaining HP: {target.health})"
        )

    def take_damage(self, amount: int) -> int:
        if self.armor is not None:
            actual_damage = max(0, amount - self.armor.defense)
        else:
            actual_damage = amount
        self.health -= actual_damage
        return actual_damage

    def is_alive(self) -> bool:
        return self._health > 0

    @abstractmethod
    def use_ability(self, target: "Hero") -> None: ...


class Warrior(Hero):
    def use_ability(self, target: "Hero") -> None:
        damage_dealt = target.take_damage(self.damage * 2)
        print(
            f"{self.name} uses Shield Bash on {target.name} for {damage_dealt} damage!"
        )


class Mage(Hero):
    def __init__(
        self, name: str, health: int, damage: int, mana: int = 50, level: int = 1
    ) -> None:
        super().__init__(name, health, damage, level)
        self.mana = mana

    def use_ability(self, target: "Hero") -> None:
        if self.mana < 10:
            raise NotEnoughManaError(f"{self.name} does not have enough mana!")
        self.mana -= 10
        damage_dealt = target.take_damage(self.damage * 3)
        print(f"{self.name} casts Fireball on {target.name} for {damage_dealt} damage!")


def battle(hero1: Hero, hero2: Hero) -> None:
    print(f"Total heroes created: {Hero.get_total_count()}")
    print("--- BATTLE START ---")
    print(f"{hero1}\nVS\n{hero2}\n")

    round_num = 1
    while hero1.is_alive() and hero2.is_alive():
        print(f"--- Round {round_num} ---")
        try:
            hero1.use_ability(hero2)
        except NotEnoughManaError as error:
            print(f"[{error}] -> Falling back to basic attack.")
            hero1.attack(hero2)

        if not hero2.is_alive():
            break

        try:
            hero2.use_ability(hero1)
        except NotEnoughManaError as error:
            print(f"[{error}] -> Falling back to basic attack.")
            hero2.attack(hero1)

        print(f"Status after round {round_num}:")
        print(f"  {hero1.name} HP: {hero1.health}")
        print(f"  {hero2.name} HP: {hero2.health}\n")
        round_num += 1

    winner = hero1 if hero1.is_alive() else hero2
    print(f"=== BATTLE OVER! Winner: {winner.name} ===")


def main() -> None:
    chainmail: Armor = Armor("ChainMail", defense=8)
    white_coat: Armor = Armor("White Coat", defense=300)
    hero1 = Mage("Gandalf", health=70, damage=15, mana=15)
    hero2 = Warrior("Conan", health=100, damage=12)
    hero1.equip_armor(white_coat)
    hero2.equip_armor(chainmail)
    battle(hero1, hero2)


if __name__ == "__main__":
    main()
