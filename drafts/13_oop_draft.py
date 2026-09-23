class Cat:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health

    def __str__(self) -> str:
        return f"Cat: {self.name} is here. HP: {self.health}/100."

    def heal(self, amount: int) -> None:
        self.health = min(100, self.health + amount)
        print(
            f"[Treatment] {self.name} was healed (+{amount} HP)! Current HP: {self.health}/100"
        )

    def meow(self) -> None:
        print(f"{self.name} says: Meow!")


class Dog:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health

    def __str__(self) -> str:
        return f"Dog: {self.name} is here. HP: {self.health}/100."

    def heal(self, amount: int) -> None:
        self.health = min(100, self.health + amount)
        print(
            f"[Treatment] {self.name} was healed (+{amount} HP)! Current HP: {self.health}/100"
        )

    def bark(self) -> None:
        print(f"{self.name} says: Woof!")


class Turtle:
    def __init__(self, name: str, health: int = 100) -> None:
        self.name: str = name
        self.health: int = health

    def __str__(self) -> str:
        return f"Turtle: {self.name} is here. HP: {self.health}/100."

    def heal(self, amount: int) -> None:
        self.health = min(100, self.health + amount)
        print(
            f"[Treatment] {self.name} was healed (+{amount} HP)! Current HP: {self.health}/100"
        )

    def hide(self) -> None:
        print(f"{self.name} hides inside its shell!")


Pet = Cat | Dog | Turtle  # short alias


class Clinic:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.patients: list[Pet] = []

    def __str__(self) -> str:
        return f"This is {self.name} clinic!"

    def add_patient(self, pet: Pet) -> None:
        self.patients.append(pet)
        print(f"[Clinic] {pet.name} was admitted to {self.name}")

    def remove_patient(self, index: int) -> None:
        index -= 1
        if index < 0 or index >= len(self.patients):  # Guard Clause
            print(f"[Clinic Error] Cannot remove. Invalid index: {index}")
            return  # 1
        removed_pet: Pet = self.patients.pop(index)
        print(f"[Clinic] {removed_pet.name} was removed from {self.name}!")

    def show_patients(self) -> None:
        print(f"\n--- {self.name} Patient List ---")
        if not self.patients:  # Guard Clause
            print("No patients in clinic.")
            return  # 1
        for index, pet in enumerate(self.patients, start=1):
            print(f"{index}. {pet}")

    def treat_patient(self, index: int, amount: int) -> None:
        index -= 1
        if index < 0 or index >= len(self.patients):  # Guard Clause 
            print("[Clinic Error] Invalid patient selection. Cannot treat")
            return  # 1
        target_pet: Pet = self.patients[index]
        print(f"\n[Clinic] Veterinarian is treating {target_pet.name}")
        target_pet.heal(amount)

    def examine_patient(self, index: int) -> None:
        index -= 1
        if index < 0 or index >= len(self.patients):  # Guard Clause
            print(f"[Clinic Error] Invalid index: {index}. Cannot examine.")
            return  # 1
        target_pet: Pet = self.patients[index]
        print(f"\n[Clinic Examination] Checking {target_pet.name}...")

        if isinstance(target_pet, Cat):
            target_pet.meow()
        elif isinstance(target_pet, Dog):
            target_pet.bark()
        elif isinstance(target_pet, Turtle):
            target_pet.hide()


#  ======================================== #
# We don't need this outer function anymore #
#  ======================================== #
def examine_pet(pet: Pet) -> None:
    print(f"\n[Vet Examination] Checking {pet}")

    if isinstance(pet, Cat):
        pet.meow()
    elif isinstance(pet, Dog):
        pet.bark()
    elif isinstance(pet, Turtle):
        pet.hide()
#  ======================================== #
# We don't need this outer function anymore #
#  ======================================== #


def main() -> None:
    #  =====================================
    print("==============")
    print("Block 1")
    print("==============")
    cat_instance: Cat = Cat("FoodLover", health=75)
    print(cat_instance)  # __str__ returns message
    dog_instance: Dog = Dog("Rex", health=80)
    print(dog_instance)  # __str__ returns message
    # = add 1 more class
    turtle_instance: Turtle = Turtle("Bob", health=95)
    print(turtle_instance)
    #  =====================================
    print("==============")
    print("Block 2")
    print("==============")
    cat_instance.meow()  # variable with object + .method(arguments)
    dog_instance.bark()  # variable with object + .method(arguments)
    # = add 1 more method
    turtle_instance.hide()
    #  =====================================
    print("==============")
    print("Block 3")
    print("==============")
    examine_pet(cat_instance)  # using standalone(outer classes) function to manage
    examine_pet(dog_instance)  # using standalone(outer classes) function to manage
    # = add 1 more condition to standalone func
    examine_pet(turtle_instance)
    #  ===================================== add 1 more class
    print("==============")
    print("Block 4")
    print("==============")
    clinic_instance: Clinic = Clinic("The Healthy Animals")
    print(clinic_instance)
    #  ===================================== add .remove/.add/.show methods
    clinic_instance.show_patients()
    clinic_instance.add_patient(cat_instance)
    clinic_instance.add_patient(dog_instance)
    clinic_instance.add_patient(turtle_instance)
    clinic_instance.show_patients()
    clinic_instance.remove_patient(1)
    clinic_instance.show_patients()
    #  ===================================== add attribute health, methods: heal, treat_patient
    print("==============")
    print("Block 5")
    print("==============")
    clinic_instance.treat_patient(1, 100)
    clinic_instance.show_patients()
    clinic_instance.examine_patient(2)
    clinic_instance.examine_patient(1)


if __name__ == "__main__":
    main()
