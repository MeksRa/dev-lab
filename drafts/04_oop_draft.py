class GymPass:
    def __init__(self, client_name: str, visits_left: int) -> None:
        self.client_name = client_name
        self.visits_left = visits_left
        self.is_active = True

    def use_visits(self) -> None:  # Guard Clauses
        if not self.is_active:  # 1
            print("Error: Gym pass is blocked/expired!")
            return  # Immediately interrupts function execution.
        if self.visits_left <= 0:  # 2
            print("Error: No visits left!")
            return  # Immediately interrupts function execution.

        self.visits_left -= 1
        print(f"Visit registered! Visits left: {self.visits_left}")
        if self.visits_left == 0:
            self.is_active = False
            print("Pass depleted and deactivated!")

    def add_visits(self, count: int) -> None:
        if count <= 0:  # Guard Clause
            print("Error: Invalid visit count.")
            return  # 1

        self.visits_left += count
        print(f"Successful! {self.client_name} has {self.visits_left} visits now.")

        if not self.is_active:
            self.is_active = True
            print("Pass successfully activated.")

    def deactivate(self) -> None:
        if self.is_active:
            self.is_active = False
            print("Pass succesfully deactivated.")
        else:
            print("Pass is already inactive.")

    def get_status(self) -> None:
        if self.is_active:
            status = "Active"
        else:
            status = "Inactive"
        print(
            f"{self.client_name} has {self.visits_left} visits left. Status: {status}."
        )


def menu() -> None:
    print("Greetings! Enter your name and the number of visits")
    gymbro1: GymPass = GymPass(input("Name: "), int(input("Visits: ")))
    while True:
        print("""
___GYM_PASS_INFO___
Options:
[Visit]
[Topup]
[Freeze]
[Status]
[Exit]
___________________
""")
        user_input = input("You: ").lower()
        if "exit" in user_input:
            break
        elif "status" in user_input:
            gymbro1.get_status()
        elif "freeze" in user_input:
            gymbro1.deactivate()
        elif "topup" in user_input:
            gymbro1.add_visits(int(input("Enter visits count to top up: ")))
        elif "visit" in user_input:
            gymbro1.use_visits()
        else:
            print("Invalid input. Try again.")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
