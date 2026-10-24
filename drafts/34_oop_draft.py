import random
from abc import ABC, abstractmethod
from typing import override


class Character(ABC):
    def __init__(self, name: str, hp: int, damage: float) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage

        self.max_hp = hp

    def attack(self, enemy: "Character") -> str:
        enemy.take_damage(self.damage)
        return f"The {self.name} performed a basic attack on the {enemy.name}! [-{self.damage}hp]"

    def take_damage(self, amount: float) -> None:
        self.hp -= amount
        self.hp = max(self.hp, 0)

    def is_alive(self) -> bool:
        return self.hp > 0

    def heal(self) -> str:
        heal_amount = int(self.max_hp * 0.5)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        return f"The {self.name} recovers, restoring 50% hp! [+{heal_amount}hp] (Current HP: {self.hp}/{self.max_hp})"

    @abstractmethod
    def special_ability(self, enemy: "Character") -> str: ...

    def __str__(self) -> str:
        return f"Hero: {self.name} | Damage: {self.damage} | HP: {self.hp}"


class Warrior(Character):
    def __init__(self, name: str, hp: int, damage: float, endurance: int) -> None:
        super().__init__(name, hp, damage)
        self.endurance = endurance

    @override
    def attack(self, enemy: "Character") -> str:
        if self.endurance >= 20:
            self.endurance -= 20
            base_report = super().attack(enemy)
            return f"{base_report} [-20 Endurance]"
        else:
            weak_damage = int(self.damage * 0.5)
            enemy.take_damage(weak_damage)
            return f"The {self.name} performed a weak attack on the {enemy.name}! [-{weak_damage}hp]"

    @override
    def special_ability(self, enemy: Character) -> str:
        if self.endurance >= 60:
            self.endurance -= 60
            special_damage = int(self.damage * 3)
            enemy.take_damage(special_damage)
            return f"The {self.name} unleashes a whirlwind of blades on the {enemy.name}! [-{special_damage}hp][-60 Endurance]"
        else:
            attack_report = self.attack(enemy)
            return f"The {self.name} attempted to use a whirlwind of blades, but to no avail! [{attack_report}]"

    @override
    def __str__(self) -> str:
        return f"{super().__str__()} | Endurance: {self.endurance}"


class Mage(Character):
    def __init__(self, name: str, hp: int, damage: float, mana: int) -> None:
        super().__init__(name, hp, damage)
        self.mana = mana

    @override
    def attack(self, enemy: "Character") -> str:
        if self.mana >= 20:
            self.mana -= 20
            base_report = super().attack(enemy)
            return f"{base_report} [-20 Mana]"
        else:
            weak_damage = int(self.damage * 0.5)
            enemy.take_damage(weak_damage)
            return f"The {self.name} performed a weak attack on the {enemy.name}! [-{weak_damage}hp]"

    @override
    def special_ability(self, enemy: Character) -> str:
        if self.mana >= 60:
            self.mana -= 60
            special_damage = int(self.damage * 3)
            enemy.take_damage(special_damage)
            return f"The {self.name} hurls a fireball the size of a house at the {enemy.name}! [-{special_damage}hp][-60 Mana]"
        else:
            attack_report = self.attack(enemy)
            return f"The {self.name} attempted to use a fireball the size of a house, but to no avail! [{attack_report}]"

    @override
    def __str__(self) -> str:
        return f"{super().__str__()} | Mana: {self.mana}"


def main() -> None:
    war = Warrior("John Great War", 500, 30, 100)
    mage = Mage("Ancient Mage", 120, 100, 100)

    # --- -- --- -- --- --
    options = ["attack", "special_ability", "heal"]

    print("==== The beggining of the battle! ====")
    print(war)
    print(mage)
    round_num = 1

    while war.is_alive() and mage.is_alive():
        print(f"--- -- Round {round_num} --- --")

        war_action = random.choice(options)
        if war_action == "attack":
            print(war.attack(mage))
        elif war_action == "special_ability":
            print(war.special_ability(mage))
        elif war_action == "heal":
            print(war.heal())

        if not mage.is_alive():
            print(f"\n{mage.name} is defeated! {war.name} has won!")
            break

        mage_action = random.choice(options)
        if mage_action == "attack":
            print(mage.attack(war))
        elif mage_action == "special_ability":
            print(mage.special_ability(war))
        elif mage_action == "heal":
            print(mage.heal())

        if not war.is_alive():
            print(f"\n{war.name} is defeated! {mage.name} has won!")
            break

        round_num += 1
        print("======================================")
    print("========= The battle is over =========")


if __name__ == "__main__":
    main()
