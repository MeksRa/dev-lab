# класс с каким-то количеством экземпляров и возможностью через меню работать с несколькими
# class
class SpaceShip:
    # Dunder Method Initializer, for modification our objects(instances)
    def __init__(self, name: str, max_shields: int) -> None:
        # Unique attributes
        self.name = name
        self.max_shields = max_shields
        # Default attributes for every ship
        self.current_shields: int = max_shields
        self.is_engine_on: bool = False

    # Methods (Functions inside the class)
    def toggle_engine(self) -> None:
        self.is_engine_on = not self.is_engine_on
        print(f"Engine has been {'started' if self.is_engine_on else 'stopped'}")

    def take_damage(self, amount: int) -> None:
        if amount <= 0:  # Guard Clause
            print("No damage was taken")
            return  # 1

        # max(0, 2-3) => max(0, -1) => 0 => returns the largest value. => min(0, -1) = -1
        self.current_shields = max(0, self.current_shields - amount)
        print(f"Took {amount} damage! Current shields: {self.current_shields}")

    def recharge_shields(self) -> None:
        if not self.is_engine_on:  # Guard Clause
            print("Error: Engine is offline!")
            return  # 1

        self.current_shields = self.max_shields
        print("Shields have been recharged!")

        # if self.is_engine_on:
        # self.current_shields = self.max_shields
        # print("Shields have been recharged!")
        # else:
        # print("Error: Engine is offline!")

    # Dunder method for print(ship instance)
    def __str__(self) -> str:
        status: str = "Online" if self.is_engine_on else "Offline"
        return f"| Ship: {self.name} | Engine: {status} | Shields: {self.current_shields}/{self.max_shields} |"


def get_damage_amount() -> int | None:
    try:
        return int(input("Enter damage amount: ").strip())
    except ValueError:
        print("Error: Please enter a valid integer number.")
        return None


# Menu 1
def select_ship_menu(fleet: list[SpaceShip]) -> None:
    while True:
        print("\n==============FLEET COMMAND==============")
        for index, ship in enumerate(fleet, start=1):
            print(f"[{index}] {ship}")
        print("[0] <- Exit game")
        print("\n=========================================")

        choice = input("Select a ship [1-5] or 0 to exit:").strip()

        if choice == "0":
            print("Shutting down Fleet command. Goodbye!")
            break

        if choice.isdigit() and 1 <= int(choice) <= len(fleet):
            selected_ship = fleet[int(choice) - 1]
            manage_ship_menu(selected_ship)
        else:
            print("Invalid ship selection. Try again.")


# Menu 2


def manage_ship_menu(ship: SpaceShip) -> None:
    while True:
        print(f"\n--- Managing: {ship.name} ---")
        print("[1] Toggle Engine")
        print("[2] Take Damage")
        print("[3] Recharge Shields")
        print("[4] View Status")
        print("[0] Back to Fleet Selection")

        choice = input(f"{ship.name}> ").strip()

        if choice == "1":
            ship.toggle_engine()
        elif choice == "2":
            damage = get_damage_amount()
            if damage is not None:
                ship.take_damage(damage)
        elif choice == "3":
            ship.recharge_shields()
        elif choice == "4":
            print(ship)
        elif choice == "0":
            print("Returning to Fleet Command...")
            break
        else:
            print("Invalid action.")


def main() -> None:
    # A list with objects(instances)
    fleet = [
        SpaceShip("Falcon", 100),
        SpaceShip("Enterprise", 150),
        SpaceShip("Apollo", 80),
        SpaceShip("Voyager", 120),
        SpaceShip("Discovery", 100),
    ]
    select_ship_menu(fleet)


if __name__ == "__main__":
    main()
