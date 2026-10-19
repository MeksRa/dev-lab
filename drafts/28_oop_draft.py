import datetime
from typing import Self


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "re" + last.lower() + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> Self:
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay))

    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        return not (day.weekday() == 5 or day.weekday() == 6)


# ---
# regular methods pass the instance (self) as the first arg
# class methods pass the class (cls) as the first arg
# static methods pass nothing automatically. Just like regular function but inside the classes
# ---

emp_1 = Employee("Max", "MeksRa", 50_000)
emp_2 = Employee("Test", "User", 60_000)

# print(Employee.raise_amount)  # 1.04
# print(emp_1.raise_amount)  # 1.04
# print(emp_2.raise_amount)  # 1.04
# Employee.set_raise_amount(1.05)
# print(Employee.raise_amount)  # 1.05
# print(emp_1.raise_amount)  # 1.05
# print(emp_2.raise_amount)  # 1.05

# ---

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane_Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
print(new_emp_1.first)

# ---

my_date = datetime.date(2026, 10, 19)
print(Employee.is_workday(my_date))
