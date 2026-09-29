# all()  # all() == True and True and True and True ...

wifi_enabled: bool = True
has_electricity: bool = True
has_subscription: bool = True
requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]
if all(requirements):
    print("Connected to internet")

people_voted: list[int] = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0]
if all(people_voted):  # u can also use "not all().."
    print("Everyone voted!")
else:
    print("Some people did not vote...")

# any()  # any() == True or False or True or False or False ...

people_voted: list[int] = [0, 1, 0, 0, 0]
if any(people_voted):
    print("At least 1 person voted")
else:
    print("No one voted...")

# isinstance()  # for comparing data types

number: int = 10
pi: float = 3.14
text: str = "banana"
my_list: list[int] = [1, 2, 3]
print(isinstance(number, int))  # True
print(isinstance(number, str))  # False
print(isinstance(number, float))  # False
print(isinstance(pi, int))  # False
print(isinstance(my_list, tuple))  # False

print(isinstance(pi, int | float))  # True  # u can use a union type |
print(isinstance(text, int | str))  # True


class Animal: ...


class Cat(Animal): ...


print(isinstance(Cat(), Animal))  # True # cat is a subclass of animal
print(isinstance(Animal(), Cat))  # False
