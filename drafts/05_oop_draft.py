# Coffee Machine


class CoffeeMachine:
    def __init__(self, water: int, coffee_beans: int) -> None:
        self.water = water
        self.coffee_beans = coffee_beans

        self.cash: float = 10
        self.is_working: bool = True

    def make_espresso(self, payment: float) -> None:
        if not self.is_working:  # Guard Clause
            print("Error: Coffee Machine is not working! Returning your money...")
            return  # 1

        if payment < 2.5:  # Guard Clause
            print(
                f"Error: Insufficient funds! Espresso costs $2.50. You inserted ${payment}"
            )
            return  # 2

        if self.water < 50:  # Guard Clause
            print("Error: Not enough water! Returning your money...")
            return  # 3

        if self.coffee_beans < 15:  # Guard Clause
            print("Error: Not enough coffee beans! Returning your money.")
            return  # 4

        self.water -= 50
        self.coffee_beans -= 15
        self.cash += 2.5
        change = payment - 2.5

        print("Enjoy your espresso! ☕")
        if change > 0:
            print(f"Here is your change: ${change:.2f}")

    def refill(self, water_amount: int = 0, beans_amount: int = 0) -> None:
        if water_amount == 0 and beans_amount == 0:  # Guard Clause
            print("Nothing to refill")
            return  # 1

        if water_amount > 0:
            self.water += water_amount
            print(f"Added {water_amount}ml of water.")
        elif water_amount < 0:
            print("Error: Water amount cannot be negative!")

        if beans_amount > 0:
            self.coffee_beans += beans_amount
            print(f"Added {beans_amount}g of coffee beans.")
        elif beans_amount < 0:
            print("Error: Beans amount cannot be negative.")

    def service(self) -> None:
        if self.is_working:
            self.is_working = False
        else:
            self.is_working = True

    def get_report(self) -> None:
        if self.is_working:
            status = "Working"
        else:
            status = "Not working"
        print(
            f"Water: {self.water}. Beans: {self.coffee_beans}. Cash: {self.cash:.2f}. Status: {status}."
        )


def menu():
    coffeemachine: CoffeeMachine = CoffeeMachine(water=200, coffee_beans=40)
    while True:
        print("""
    __________________
    __Coffee Machine__
    Options: 
    [Buy]
    [Refill]
    [Report]
    [Exit]
    __________________

    """)
        user_input = input("User: ").lower()
        if "exit" in user_input:
            print("The coffee machine is turning off... Bye!")
            break

        elif "buy" in user_input:
            print("The price of an espresso is $2.50.")
            money = input("Insert money: ")
            coffeemachine.make_espresso(float(money))

        elif "refill" in user_input:
            print(
                "What do you want to refill it with?\n[1] <- Water\n[2] <- Beans\n[3] <- Both"
            )
            refill_choice = input("User: ").lower()
            print(refill_choice)
            if "1" in refill_choice:
                coffeemachine.refill(
                    water_amount=int(input("Enter the amount of water: "))
                )
            elif "2" in refill_choice:
                coffeemachine.refill(
                    beans_amount=int(input("Enter the amount of beans: "))
                )
            elif "3" in refill_choice:
                coffeemachine.refill(
                    water_amount=int(input("Enter the amount of water: ")),
                    beans_amount=int(input("Enter the amount of beans: ")),
                )
            else:
                print("Invalid input.")
        elif "report" in user_input:
            coffeemachine.get_report()
        elif "service" in user_input:
            coffeemachine.service()
        else:
            print("Invalid input. Try again.")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
