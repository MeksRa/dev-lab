# from abc import ABC


class Character:
    def __init__(self, health: int, damage: int, speed: int) -> None:
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self, amount: float) -> None:
        self.health -= amount


class Warrior(Character):
    def __init__(self, health, damage, speed):
        super().__init__(health, damage, speed)
        self.toughness_modifier = 0.90

    def take_damage(self, amount: float) -> None:
        modified_amount = amount * self.toughness_modifier
        super().take_damage(modified_amount)


warrior = Warrior(100, 50, 50)
print(f"Initial health: {warrior.health}")
warrior.take_damage(40)
print(f"Health after damage: {warrior.health}")
