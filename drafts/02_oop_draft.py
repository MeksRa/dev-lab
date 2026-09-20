# Bank Account oop script


class BankAccount:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.balance = 0
        self.is_blocked = False

    def deposit(self, amount: float) -> None:
        if self.is_blocked:
            print(f"Account of {self.owner} is blocked! Cannot deposit")
        else:
            self.balance += amount
            print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount: float) -> None:
        if self.is_blocked:
            print(f"Account of {self.owner} is blocked! Cannot withdraw")
        elif self.balance < amount:
            print(
                f"Not enough money! {self.owner} tried to withdraw ${amount}, but balance is ${self.balance}"
            )
        else:
            self.balance -= amount
            print(
                f"{self.owner} withdrew ${amount}. Remaining balance: ${self.balance}"
            )

    def block(self) -> None:
        self.is_blocked = True
        print(f"Account of {self.owner} has been blocked")


def menu() -> None:
    user: BankAccount = BankAccount("Max")
    while True:
        print("---Your Bank---")
        print("""Choose an option:
01. [Check] your balance
02. [Withdraw]
03. [Deposit]
04. [Block] your account
05. [Exit]
""")
        print("---------------")
        user_choice = input(f"{user.owner}: ").lower()
        if "check" in user_choice:
            print(user.balance)
        elif "withdraw" in user_choice:
            money = int(input(f"{user.owner}, enter the ammout to withdraw: "))
            user.withdraw(money)
        elif "deposit" in user_choice:
            money = int(input(f"{user.owner}, enter the ammout to deposit: "))
            user.deposit(money)
        elif "block" in user_choice:
            user.block()
        elif "exit" in user_choice:
            print("Bye")
            break
        else:
            print("Invalid input. [Options: check/withdraw/deposit/exit]")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
