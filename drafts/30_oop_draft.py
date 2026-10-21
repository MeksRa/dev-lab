class Employee:
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "re" + last.lower() + "@gmail.com"

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self) -> str:
        # For developers
        # Output:
        # Employee('Max', 'MeksRa', '50000')
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self) -> str:
        # For users
        # Output:
        # Max MeksRa - remeksra@gmail.com
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other: "Employee") -> int:
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.fullname())

emp_1 = Employee("Max", "MeksRa", 50_000)
emp_2 = Employee("Max_2", "MeksRa_2", 60_000)

print(emp_1)  # Max MeksRa - remeksra@gmail.com
print(repr(emp_1))  # Employee('Max', 'MeksRa', '50000')
print(str(emp_1))  # Max MeksRa - remeksra@gmail.com
print(emp_1.__repr__())  # Employee('Max', 'MeksRa', '50000')
print(emp_1.__str__())  # Max MeksRa - remeksra@gmail.com

# --
print(1 + 2)  # 3 
print(int.__add__(1, 2))  # 3
print(str.__add__("a", "b"))  # 'ab'
print(emp_1 + emp_2)  # 110000  => using our __add__ method

print(len("test"))  # 4
print("test".__len__())  # 4
print(len(emp_1))  # 10  => using our __len__ method