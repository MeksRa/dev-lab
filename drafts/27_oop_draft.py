class Employee:
    # __init__ receive instance (self) as a first argument
    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "re" + last.lower() + "@gmail.com"

    def fullname(self) -> str:
        return f"{self.first} {self.last}"


emp_1 = Employee("Max", "MeksRa", 50_000)
emp_2 = Employee("Test", "User", 60_000)


print(Employee.fullname(emp_1))
print(emp_1.fullname())

# --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- --- -- ---
