class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last
        # self.email = first + "_re" + last.lower() + "@gmail.com"

    # defining like a method
    # accessing like its an atribute (w/o '()')
    @property
    def email(self) -> str:
        return f"{self.first}_re{self.last}@gmail.com"

    @property  # getter
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @fullname.setter  # setter
    def fullname(self, name: str) -> None:
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter  # deleter
    def fullname(self) -> None:
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee("Max", "MeksRa")
emp_1.fullname = "Meksra Max"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname