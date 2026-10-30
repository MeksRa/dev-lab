from typing import override


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = initial_balance  # uses a setter

    # --- -- ---

    # @property (getter) is how you read a value from the outside
    # (it looks like a variable—e.g.,
    # `obj.balance`—but under the hood,
    # it returns a hidden field).
    @property
    def balance(self) -> float:
        return self._balance

    # @balance.setter is how you define the assignment of a value
    # (it intercepts the operation `obj.balance = 100`
    # and checks whether the value is valid).
    @balance.setter
    def balance(self, new_balance: float) -> None:
        if new_balance < 0:
            raise ValueError("The balance cannot be negative!")
        self._balance = new_balance

    # --- -- ---

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The deposit amount must be greater than zero!")
        self.balance += amount  # uses @property (setter)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The withdrawal amount must be greater than zero!")
        if amount > self._balance:
            raise ValueError("Insufficient funds in the account!")
        self._balance -= amount


class CreditAccount(BankAccount):
    def __init__(
        self, owner: str, initial_balance: float = 0.0, credit_limit: float = 0.0
    ) -> None:
        super().__init__(owner, initial_balance)
        self.credit_limit = credit_limit

    # Override the withdrawal method to allow the balance to go negative, up to a specified limit
    @override
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("The withdrawal amount must be greater than zero!")

        # Available amount = current balance + credit limit
        available_funds = self._balance + self.credit_limit
        if amount > available_funds:
            raise ValueError("Credit limit exceeded!")

        # Withdrawing funds: if the balance goes into the negative, the amount is deducted from the credit limit
        self._balance -= amount


# --- -- --- -- ---
def main() -> None:
    # Bank Account
    acc = BankAccount("Ivan", 10_000)
    acc.deposit(500)
    acc.withdraw(2000)
    print(f"Balance {acc.owner}: {acc.balance}")  # 8500.0
    # Credit Account
    credit_acc = CreditAccount("Anna", initial_balance=1_000, credit_limit=10_000)
    print(f"Credit Score {credit_acc.owner} has been created.")

    # We withdraw more than the available balance,
    # but stay within the credit limit (resulting in a balance of -4000)
    credit_acc.withdraw(5_000)
    print(
        f"Balance after going into the negative: {credit_acc._balance}"
    )  # -4000.0 (fell into the negative due to a loan)


if __name__ == "__main__":
    main()
