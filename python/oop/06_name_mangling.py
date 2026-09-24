class Account:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.__balance = balance  # transforms into "_Account__balance"
        # tells python that he should mangle this name
        # Mangle to avoid naming collisions

    def deposit(self, amount: int) -> None:
        self.__balance += amount
        print(f"${amount} deposited into main.")

    def get_balance(self) -> None:
        print(f"Main: ${self.__balance}")


class Savings(Account):
    def __init__(self, owner: str) -> None:
        super().__init__(owner, balance=0)

        self.__balance = 0  # Transforms into "_Savings__balance"

    def deposit_into_savings(self, amount: int) -> None:
        self.__balance += amount
        print(f"${amount} deposited into savings.")

    def get_savings_balance(self) -> None:
        print(f"Savings: ${self.__balance}")


account: Savings = Savings("Charlie")

account.deposit(500)
account.deposit_into_savings(4000)

account.get_balance()  # Main: $500
account.get_savings_balance()  # Savings: $4000

account.deposit(500)

account.get_balance()  # Main: $1000
account.get_savings_balance()  # Savings: $4000

# print(account._Account__balance)  # 1000 # Python mangles "__balance" into this
# print(account._Savings__balance)  # 4000 # Python mangles "__balance" into this


# ======================================= Second example

from uuid import UUID, uuid4

print(uuid4())  # Create unique identifier


class Product:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__unique_id = self.__create_unique_id()

    def __create_unique_id(self) -> UUID:
        print(f'Product: "{self.name}" has been created!')
        return uuid4()

    # 1
    def compare_product(self, other: "Product") -> bool:
        print(f"{self.name}: {self.__unique_id}")
        print(f"{other.name}: {other.__unique_id}")
        return self.__unique_id == other.__unique_id

    # 2
    def display_id(self) -> None:
        print(f"{self.name}: {self.__unique_id}")

    # 3  # classic getter
    def get_id(self) -> UUID:
        return self.__unique_id


cup: Product = Product("Cup")
hat: Product = Product("Hat")
print(cup.compare_product(hat))  # 1
cup.display_id()  # 2
print(cup.get_id())  # 3
