from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override

# =========================================== #
# ______________<-__Animal__->______________  #
# __<-_Feathered_->_________<-_Mammal_->____  #
# _Bird_______Dragon______Dog_________Human_  #
# =========================================== #


@dataclass
class Habitat:
    biome: str
    temperature: float
    is_safe: bool = True


class Animal(ABC):
    def __init__(
        self, name: str, age: int, energy: int = 100, habitat: Habitat | None = None
    ):
        self.name = name
        self.age = age  # Triggers property setter with validation
        self.energy = energy

        self.habitat = habitat or Habitat(biome="Wild Plains", temperature=20.0)

    @property  # Getter for age property
    def age(self) -> int:
        return self._age

    @age.setter  # Setter for age property with validation
    def age(self, value: int):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

    @classmethod
    def spawn_baby(cls, name: str, biome: str) -> "Animal":
        """An alternative constructor for creating a baby animal with a default age of 0"""
        baby_habitat = Habitat(biome=biome, temperature=22.0)
        # cls(...) will call the constructor of the class on which the method was invoked (for example, Dragon or Bird)
        return cls(name=name, age=0, energy=100, habitat=baby_habitat)

    @staticmethod
    def validate_name(name: str) -> bool:
        """Utility method to check if a name is non-empty and capitalized."""
        return bool(name and name.istitle())

    @abstractmethod
    def makes_sound(self) -> str: ...

    @abstractmethod
    def moves(self) -> str: ...

    @abstractmethod
    def describe(self) -> str: ...

    def train(self) -> str:
        return f"'{self.name}' is training. Energy level: {self.energy}"


class Feathered(Animal):
    def __init__(
        self,
        name: str,
        age: int,
        energy: int = 100,
        wingspan: int = 50,
        habitat: Habitat | None = None,
    ):
        super().__init__(name, age, energy, habitat)
        self.wingspan = wingspan

    @override
    def moves(self) -> str:
        return f"'{self.name}' is flying away."


class Bird(Feathered):
    @override
    def makes_sound(self) -> str:
        return f"'{self.name}' sings"

    @override
    def describe(self) -> str:
        return f"'{self.name}' is a bird. Age: {self.age}. Wingspan: {self.wingspan}."

    def flip(self) -> str:
        return f"'{self.name}' makes a flip"


class Dragon(Feathered):
    def __init__(
        self,
        name: str,
        age: int,
        energy: int = 100,
        wingspan: int = 150,
        flame_power: int = 500,
        habitat: Habitat | None = None,
    ):
        super().__init__(name, age, energy, wingspan, habitat)
        self.flame_power = flame_power

    @override
    def makes_sound(self) -> str:
        return f"'{self.name}' growls."

    @override
    def describe(self) -> str:
        return (
            f"'{self.name}' is a dragon. Age: {self.age}. "
            f"Flame Power: {self.flame_power}. "
            f"Biome: {self.habitat.biome} (Temp: {self.habitat.temperature}°C)"
        )

    def fireball(self) -> str:
        return f"'{self.name}' spews fire."

    @override
    def train(self) -> str:
        base_result = super().train()
        self.flame_power += 10
        return (
            f"{base_result} | Flame power increased! Current power: {self.flame_power}"
        )


class Mammal(Animal):
    def jump(self) -> str:
        return f"'{self.name}' jumps"


class Dog(Mammal):
    @override
    def makes_sound(self) -> str:
        return f"'{self.name}' barks"

    @override
    def moves(self) -> str:
        return f"'{self.name}' is running on four paws."

    @override
    def describe(self) -> str:
        return f"'{self.name}' is a dog. Age: {self.age}"


class Human(Mammal):
    @override
    def makes_sound(self) -> str:
        return f"'{self.name}' talks a lot"

    @override
    def moves(self) -> str:
        return f"'{self.name}' is running on his legs."

    @override
    def describe(self) -> str:
        return f"'{self.name}' is a Human. Age: {self.age}"


# --- -- --- -- --- -- --- -- ---


def main() -> None:
    print("===== WELCOME TO THE ZOO =====")

    # 1. Validate names using the static method
    names = ["Deathwing", "rex", "Rio"]
    print("\n[Static Method Check - Name Validation]")
    for name in names:
        is_valid = Animal.validate_name(name)
        print(f"Name '{name}' is valid: {is_valid}")

    # 2. Setup Habitats via Dataclass and spawn animals using regular init & classmethod
    volcano_habitat = Habitat(biome="Volcano Cave", temperature=450.5, is_safe=False)

    zoo_animals = [
        Dragon(name="Deathwing", age=150, flame_power=850, habitat=volcano_habitat),
        Bird(name="Rio", age=2, wingspan=35),
        Dog(name="Rex", age=5),
        Human(name="Alice", age=28),
        # Using classmethod alternative constructor for a baby bird
        Bird.spawn_baby(name="Chippy", biome="Tropical Canopy"),
    ]

    # 3. Simulate the Zoo Loop (Polymorphism & Property protection)
    print("\n[Zoo Daily Routine Simulation]:")
    for animal in zoo_animals:
        print("==============================")
        print(animal.describe())
        print(f"Sound: {animal.makes_sound()}")
        print(f"Movement: {animal.moves()}")
        print(animal.train())

        # Triggering specific unique methods if available
        if isinstance(animal, Dragon):
            print(f"Special action: {animal.fireball()}")
        elif isinstance(animal, Bird):
            print(f"Special action: {animal.flip()}")

    # 4. Testing property validation (age security)
    print("\n[Property Security Test]:")
    try:
        zoo_animals[0].age = -5  # Trying to set an invalid negative age
    except ValueError as e:
        print(f"Caught error successfully: {e}")


if __name__ == "__main__":
    main()


# OUTPUT:
# ===== WELCOME TO THE ZOO =====

# [Static Method Check - Name Validation]
# Name 'Deathwing' is valid: True
# Name 'rex' is valid: False
# Name 'Rio' is valid: True

# [Zoo Daily Routine Simulation]:
# ==============================
# 'Deathwing' is a dragon. Age: 150. Flame Power: 850. Biome: Volcano Cave (Temp: 450.5°C)
# Sound: 'Deathwing' growls.
# Movement: 'Deathwing' is flying away.
# 'Deathwing' is training. Energy level: 100 | Flame power increased! Current power: 860
# Special action: 'Deathwing' spews fire.
# ==============================
# 'Rio' is a bird. Age: 2. Wingspan: 35.
# Sound: 'Rio' sings
# Movement: 'Rio' is flying away.
# 'Rio' is training. Energy level: 100
# Special action: 'Rio' makes a flip
# ==============================
# 'Rex' is a dog. Age: 5
# Sound: 'Rex' barks
# Movement: 'Rex' is running on four paws.
# 'Rex' is training. Energy level: 100
# ==============================
# 'Alice' is a Human. Age: 28
# Sound: 'Alice' talks a lot
# Movement: 'Alice' is running on his legs.
# 'Alice' is training. Energy level: 100
# ==============================
# 'Chippy' is a bird. Age: 0. Wingspan: 50.
# Sound: 'Chippy' sings
# Movement: 'Chippy' is flying away.
# 'Chippy' is training. Energy level: 100
# Special action: 'Chippy' makes a flip

# [Property Security Test]:
# Caught error successfully: Age cannot be negative!
