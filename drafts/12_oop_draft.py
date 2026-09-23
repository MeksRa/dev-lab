# Hangars and Fighters


class Fighter:
    def __init__(self, model: str, max_health: int) -> None:
        self.model: str = model
        self.max_health: int = max_health

        self.current_health: int = self.max_health
        self.is_docked: bool = False

    def repair(self) -> None:
        if not self.is_docked:
            print("\nThe fighter isn't docked!")
            return
        self.current_health = self.max_health
        print(f"\n{self.model} has just been repaired!")

    def take_damage(self, amount: int) -> None:
        if amount <= 0:  # Guard Clause
            print("\nNo damage was taken!")
            return  # 1
        self.current_health = max(0, self.current_health - amount)

    def __str__(self) -> str:
        status: str = "Docked" if self.is_docked else "Undocked"
        return f"Ship: {self.model} | Health: {self.current_health}/{self.max_health} | Status: {status}"


def get_damage_amount() -> int | None:
    try:
        return int(input("Enter damage amount: ").strip())
    except ValueError:
        print("\nError: Please enter a valid integer number.")
        return None


class Hangar:
    def __init__(self, name: str, capacity: int) -> None:
        self.name: str = name
        self.capacity: int = capacity

        self.ships: list[Fighter] = []

    def add_ship(self, ship: Fighter) -> None:
        if len(self.ships) >= self.capacity:  # Guard Clause
            print(f"\nThe {self.name} is full!")
            return  # 1
        if ship.is_docked:  # Guard Clause
            print(f"\n{ship.model} is already docked!")
            return  # 2

        ship.is_docked = True
        self.ships.append(ship)
        print(f"\n{ship.model} has just been docked!")

    def remove_ship(self, ship: Fighter) -> None:
        if not ship.is_docked:  # Guard Clause
            print(f"\n{ship.model} isn't docked")
            return  # 1
        ship.is_docked = False
        self.ships.remove(ship)
        print(f"\n{ship.model} has just been removed!")

    def __str__(self) -> str:
        return f"Hangar: {self.name}. ({len(self.ships)}/{self.capacity})"


# Menu #1
def hangars(all_ships: list[Fighter], all_hangars: list[Hangar]) -> None:
    while True:
        print("===========================================")
        print("The “Last Hope” Space Station welcomes you!")
        hangar_indexes = []
        for index, hangar in enumerate(all_hangars, 1):
            print(f"[{index}] <= {hangar}")
            hangar_indexes.append(str(index))
        print("[0] <= Exit")
        print("===========================================")
        user_input: str = input("Select a hangar: ").strip()
        if "0" == user_input:
            print("Goodbye, Commander!")
            break
        elif user_input in hangar_indexes:
            manage_hangar(all_ships, all_hangars[int(user_input) - 1])
        else:
            print("Invalid input")


# Menu #2
def manage_hangar(all_ships: list[Fighter], choiced_hangar: Hangar) -> None:
    while True:
        available_ships = [ship for ship in all_ships if not ship.is_docked]
        print("""
==========================================================================
| [0] Return | [1] Add | [2] Remove | [3] Repair | [4] Damage | [5] Show |
==========================================================================
""")
        user_input = input("Commander: ").strip()

        if user_input == "1":  # Add
            if not available_ships:
                print("No available ships to dock!")
                continue
            print("======== Available ships ========")
            for index, ship in enumerate(available_ships, 1):
                print(f"[{index}] {ship}")
            print("=================================")
            user_choice = input("Which vessel would you like to add? ").strip()
            if not user_choice.isdigit() or not (
                0 <= (int(user_choice) - 1) < len(available_ships)
            ):
                print("Invalid input")
                continue
            choiced_hangar.add_ship(available_ships[int(user_choice) - 1])

        elif user_input == "2":  # Remove
            if not choiced_hangar.ships:
                print("Cannot remove a ship. It's empty")
            else:
                print(f"=== Ships in {choiced_hangar} ===")
                for index, ship in enumerate(choiced_hangar.ships, 1):
                    print(f"{index} - {ship}")
                print("=================================")
                user_choice = input("Which vessel would you like to remove? ").strip()
                if not user_choice.isdigit() or not (
                    0 <= (int(user_choice) - 1) < len(choiced_hangar.ships)
                ):
                    print("Invalid input")
                    continue
                choiced_hangar.remove_ship(choiced_hangar.ships[int(user_choice) - 1])

        elif user_input == "3":  # Repair
            if not choiced_hangar.ships:
                print("The hangar is empty. There is nothing to repair")
                continue
            else:
                print(f"=== Ships in {choiced_hangar} ===")
                for index, ship in enumerate(choiced_hangar.ships, 1):
                    print(f"{index} - {ship}")
                print("=================================")
                user_choice = input("Which vessel would you like to repair? ").strip()
                if not user_choice.isdigit() or not (
                    0 <= (int(user_choice) - 1) < len(choiced_hangar.ships)
                ):
                    print("Invalid input")
                    continue
                choiced_hangar.ships[int(user_choice) - 1].repair()

        elif user_input == "4":  # Damage
            if not choiced_hangar.ships:
                print("The hangar is empty. There are no ships here...")
                continue
            else:
                print(f"=== Ships in {choiced_hangar} ===")
                for index, ship in enumerate(choiced_hangar.ships, 1):
                    print(f"{index} - {ship}")
                print("=================================")
                user_choice = input("Which vessel was damaged? ").strip()
                if not user_choice.isdigit() or not (
                    0 <= (int(user_choice) - 1) < len(choiced_hangar.ships)
                ):
                    print("Invalid input")
                    continue
                damage = get_damage_amount()
                if damage is not None:
                    choiced_hangar.ships[int(user_choice) - 1].take_damage(damage)

        elif user_input == "5":  # Show
            if not choiced_hangar.ships:
                print("Empty")
            else:
                for ship in choiced_hangar.ships:
                    print(f" - {ship}")

        elif user_input == "0":  # Return
            break


def main() -> None:
    all_ships: list = [
        Fighter("X-Wing", 120),
        Fighter("TIE Fighter", 80),
        Fighter("Millennium Falcon", 200),
        Fighter("Y-Wing", 150),
        Fighter("Razor Crest", 180),
    ]
    all_hangars: list = [
        Hangar("Alpha Dock", 2),
        Hangar("Main Bay", 4),
        Hangar("Repair Outpost", 1),
    ]
    hangars(all_ships, all_hangars)


if __name__ == "__main__":
    main()
