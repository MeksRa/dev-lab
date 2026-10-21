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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(
        self, first: str, last: str, pay: int, employees: list[Employee] | None = None
    ) -> None:
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee) -> None:
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self) -> None:
        for emp in self.employees:
            print("-->", emp.fullname())


# w/o super()
# dev_1 = Developer("Max", "MeksRa", 50_000)
# dev_2 = Employee("Max_2", "MeksRa_2", 50_000)
# print(help(Developer))

# print(dev_1.pay)  # 50_000
# print(dev_2.pay)  # 50_000
# dev_1.apply_raise()
# dev_2.apply_raise()
# print(dev_1.pay)  # 55_000  => by 10%
# print(dev_2.pay)  # 52_000  => by 4%

# w super()
dev_1 = Developer("Max", "MeksRa", 50_000, "Python")
dev_2 = Developer("Max_2", "MeksRa_2", 50_000, "Java")

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr_1 = Manager("Sue", "Smith", 90_000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# ---
print(
    isinstance(mgr_1, Manager)
)  # ask if the mgr_1 is instance of the Manager  # => True

print(
    issubclass(Developer, Employee)
)  # ask if the Developer is subclass of Employee  # => True
