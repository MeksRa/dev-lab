class BankAccount:
    def __init__(self, account_name: str, pin_code: str) -> None:
        self.account_name: str = account_name
        self.pin_code: str = pin_code

        self.balance: float = 0.0
        self.is_active: bool = True  # Blocked | Active

    def deposit(self, amount: float, entered_pin_code: str) -> None:
        if not self.is_active:  # Guard Clause
            print("You cannot top up a blocked account.")
            return  # 1

        if entered_pin_code != self.pin_code:  # Guard Clause
            print("Entered Pin Code is incorrect!")
            return  # 2
        if amount <= 0:  # Guard Clause
            print("Entered incorrect amount!")
            return  # 3

        self.balance += amount
        print(f"Your balance has just been topped up by ${amount}")

    def withdraw(self, amount: float, entered_pin_code: str) -> None:
        if not self.is_active:
            print("You cannot make withdrawals from a blocked account.")
            return  # 1

        if entered_pin_code != self.pin_code:
            print("Entered Pin Code is incorrect!")
            return  # 2
        if amount <= 0:
            print("Entered incorrect amount!")
            return
        if amount > self.balance:
            print("You cannot withdraw more than the available balance!")
            return

        self.balance -= amount
        print(f"${amount} has just been deducted from the balance.")

    def __str__(self) -> str:
        status: str = "Active" if self.is_active else "Blocked"
        return f"| User: {self.account_name} | Balance: ${self.balance} | Status: {status} |"

    def blocker(self, entered_pin_code) -> None:

        if entered_pin_code != self.pin_code:  # Guard Clause
            print("Entered Pin Code is incorrect!")
            return  # 1
        if self.is_active:
            self.is_active = False
            print("Your account has just been blocked!")
        else:
            self.is_active = True
            print("Your account has just been unblocked!")


def get_pin_and_amount(prompt_action: str) -> tuple[str, float] | None:
    entered_pin_code = input("Enter the Pin Code: ").strip()
    if not (entered_pin_code.isdigit() and len(entered_pin_code) == 4):
        print("Error: The PIN code must consist of 4 digits.")
        return None
    try:
        amount = float(input(f"Enter the amount to {prompt_action}: ").strip())
        return entered_pin_code, amount
    except ValueError:
        print("Error: The amount must be a number.")
        return None


def menu():
    bankaccount1: BankAccount = BankAccount("Max", "1234")
    while True:
        print("""
===================
=====Your Bank=====
[0] <- Exit
[1] <- Deposit
[2] <- Withdraw
[3] <- Status
[4] <- Block account
===================
""")
        user_input: str = input(f"{bankaccount1.account_name}: ")
        if "0" == user_input:
            print("Bye!")
            break

        elif user_input in ("1", "2"):
            action = "deposit" if user_input == "1" else "withdraw"
            data = get_pin_and_amount(action)
            if data:
                pin, amount = data
                if user_input == "1":
                    bankaccount1.deposit(amount, pin)
                else:
                    bankaccount1.withdraw(amount, pin)

        elif "3" == user_input:
            print(bankaccount1)
        elif "4" == user_input:
            entered_pin_code = input("Enter the Pin Code: ").strip()
            if not (entered_pin_code.isdigit() and len(entered_pin_code) == 4):
                print("Error: The PIN code must consist of 4 digits.")
                continue
            bankaccount1.blocker(entered_pin_code)
        else:
            print("Invalid input")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
