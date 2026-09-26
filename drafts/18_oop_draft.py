from abc import ABC, abstractmethod


class Hero(ABC):  # "ABC" prevents inheritance without an abstract method
    def __init__(self, name: str, hp: int, damage: int) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage

    def introduce(self) -> None:
        print(f"Hello! I'm {self.name}. I have {self.hp} hp.")

    @abstractmethod
    def attack(self, target: "Hero") -> None: ...


class Warrior(Hero):
    def __init__(self, name: str, hp: int, damage: int, armor: int) -> None:
        super().__init__(name, hp, damage)  # Passing name and hp to the parent "Hero".
        self.armor = armor

    def attack(self, target: Hero) -> None:
        print(f"{self.name} attacks {target.name} with sword for {self.damage} damage!")
        target.hp -= self.damage

    def introduce(self) -> None:
        super().introduce()  # Extending the parent class
        print(f"Armor level: {self.armor}")


class Mage(Hero):
    def __init__(self, name: str, hp: int, damage: int, mana: int) -> None:
        super().__init__(name, hp, damage)  # Passing name and hp to the parent "Hero".
        self.mana = mana

    def attack(self, target: Hero) -> None:
        print(f"{self.name} casts spell on {target.name} for {self.damage} damage!")
        target.hp -= self.damage

    def introduce(self) -> None:
        super().introduce()  # Extending the parent class
        print(f"Mana pool: {self.mana}")


hero1: Hero = Warrior("Nagibator", 375, 73, 100)
hero2: Hero = Mage("Gendalf", 83, 263, 100)

print("-- -- -- --")
hero1.introduce()  # parent's method
hero2.introduce()  # parent's method
print("-- -- -- --")
hero1.attack(hero2)  # warrior's method
print("-- -- -- --")
hero2.attack(hero1)  # mage's method
print("-- -- -- --")
hero1.introduce()  # parent's method
hero2.introduce()  # parent's method
print("-- -- -- --")
