# ==============
# 01) callable()
# ==============

fruit: str = "apple"
number: int = 10


def func() -> None:
    print("func() was called")


print(f"callable(): {callable(fruit)}")  # callable(): False
print(f"callable(): {callable(number)}")  # callable(): False

print(f"callable(): {callable(func)}")  # callable(): True
print(f"callable(): {callable(range)}")  # callable(): True
print(f"callable(): {callable(str)}")  # callable(): True
if callable(func):
    func()
else:
    print("Object is not callable")

# ==============
# 02) filter()
# ==============

numbers: list[int] = list(range(1, 21))
print(numbers)


def is_even(number: int) -> bool:
    return number % 2 == 0


even_numbers: filter = filter(is_even, numbers)
print(even_numbers)  # <filter object at 0x0000020E4D4F5BD0>
print(list(even_numbers))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# lambda <parameter>: <functionality>, list
even_numbers_lambda: filter = filter(lambda n: n % 2 == 0, numbers)
print(even_numbers_lambda)  # <filter object at 0x0000020E4D4F5BD0>
print(list(even_numbers_lambda))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

people: list[str] = ["Anna", "Bob", "Betty", "James", "John"]
long_names: filter = filter(lambda name: len(name) > 4, people)
print(long_names)  # <filter object at 0x000001A3467F6410>
print(list(long_names))  # ['Betty', 'James']

ln_list_comprehension: list[str] = [name for name in people if len(name) > 4]
print(ln_list_comprehension)  # ['Betty', 'James']

# ==============
# 03) map()
# ==============

numbers: list[int] = [1, 2, 3, 4, 5]


def double(number: int) -> int:
    return number * 2


doubled: map = map(double, numbers)
print(doubled)  # <map object at 0x0000025BCA65E7C0>
print(list(doubled))  # [2, 4, 6, 8, 10]

doubled_lambda: map = map(lambda n: n * 2, numbers)  # noqa: C417
print(doubled_lambda)  # <map object at 0x0000025BCA65E7C0>
print(list(doubled_lambda))  # [2, 4, 6, 8, 10]

# [double(n) for n in numbers]
doubled_list_comprehension: list[int] = [n * 2 for n in numbers]
print(doubled_list_comprehension)  # [2, 4, 6, 8, 10]

numbers: list[int] = [1, 2, 3, 4, 5]
letters: list[str] = ["a", "b", "c"]


def combine_elements(number: int, letter: str) -> tuple[int, str]:
    return number, letter


combined: map = map(combine_elements, numbers, letters)
print(list(combined))  # [(1, 'a'), (2, 'b'), (3, 'c')]

combined_lambda: map = map(lambda n, l: (n, l), numbers, letters)
print(list(combined_lambda))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# ==============
# 04) sorted()  | better than list comprehension
# ==============

numbers: list[int] = [1, 10, 5, 3]
people: list[str] = ["Mario", "James", "Anna"]

sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers)  # [1, 3, 5, 10] -> ascending order
sorted_names: list[str] = sorted(people)
print(sorted_names)  # ['Anna', 'James', 'Mario'] -> alphabetical order(ascii value)

people: list[str] = ["Mario", "James", "anna"]
sorted_names: list[str] = sorted(people)  # "A" - 65 / "a" - 97
print(sorted_names)  # ['James', 'Mario', 'anna'] -> alphabetical order(ascii value)

sorted_names: list[str] = sorted(people, reverse=True)  # reversed
print(sorted_names)  # ['anna', 'Mario', 'James']

people: list[str] = ["Mario", "James", "Anna", "Tom"]
sorted_names: list[str] = sorted(people, key=lambda x: len(x))
print(sorted_names)  # ['Tom', 'Anna', 'Mario', 'James']


class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.name}={self.weight}kg"


cat: Animal = Animal("Cat", 10)
dog: Animal = Animal("Dog", 5)
kangaroo: Animal = Animal("Kangaroo", 50)

sorted_animals: list[Animal] = sorted(
    [cat, dog, kangaroo], key=lambda animal: animal.weight
)
print(sorted_animals)  # [Dog=5kg, Cat=10kg, Kangaroo=50kg]

# ==============
# 05) zip()
# ==============

numbers: list[int] = [1, 2, 3, 4]
letters: list[str] = ["A", "B", "C", "D"]
symbols: list[str] = ["!", "@", "$"]

zipped: zip = zip(numbers, letters)
# print(zipped)  # <zip object at 0x000001FF3514FC80>
# print(list(zipped))  # [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]

for n, l in zipped:
    print(n, l, sep=": ")
# 1: A
# 2: B
# 3: C
# 4: D

zipped: zip = zip(numbers, symbols)  # ,<strict=True> for all elements
# but get ValueError if u haven't enough pairs of elements to zip together
print(list(zipped))  # [(1, '!'), (2, '@'), (3, '$')]
zipped: zip = zip(numbers, symbols, letters, strict=False)
print(list(zipped))  # [(1, '!', 'A'), (2, '@', 'B'), (3, '$', 'C')]
