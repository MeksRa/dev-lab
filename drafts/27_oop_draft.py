class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    # __init__ receive instance (self) as a first argument
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


print(Employee.num_of_emps)  # 0
emp_1 = Employee("Max", "MeksRa", 50_000)
emp_2 = Employee("Test", "User", 60_000)
emp_3 = Employee("Test_2", "User_2", 70_000)
print(Employee.num_of_emps)  # 3

# print(Employee.fullname(emp_1))
# print(emp_1.fullname())

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
# {'first': 'Max', 'last': 'MeksRa', 'pay': 50000, 'email': 'remeksra@gmail.com'}

# print(Employee.__dict__)

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06
emp_2.raise_amount = 1.07
Employee.raise_amount = 1.05

print(emp_1.__dict__)
# {'first': 'Max', 'last': 'MeksRa', 'pay': 50000, 'email': 'remeksra@gmail.com', 'raise_amount': 1.06}

print(Employee.raise_amount, "Employee")  # 1.05
print(emp_1.raise_amount, "emp_1")  # 1.06
print(emp_2.raise_amount, "emp_2")  # 1.07
print(emp_3.raise_amount, "emp_3")  # 1.05

# -------
