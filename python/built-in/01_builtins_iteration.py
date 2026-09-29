# 81-85

# print()

print(1, 2, "A", True, ["a", "b"], sep="-", end="!!!\n")  # 1-2-A-True-['a', 'b']!!!
people: list[str] = ["Mario", "James", "Hannah"]
print(*people)  # == print("Mario", "James", "Hannah")  # Mario James Hannah
print(*people, sep=", ", end=".")  # Mario, James, Hannah.

# enumerate

elements: list[str] = ["A", "B", "C"]
enumeration: enumerate = enumerate(elements, start=1)
print(list(enumeration))  # [(1, 'A'), (2, 'B'), (3, 'C')]

for i, element in enumerate(elements, start=1):
    print(f"{i}: {element}")
# 1: A
# 2: B
# 3: C

# round()

a: float = 200.343243
b: float = 18.12321
c: float = 47.59333
result: float = a + b + c  # 266.059783
print(round(result, 2))  # 266.06
print(round(result, 1))  # 266.1
print(round(result, 0))  # 266.0
print(round(result, -1))  # 270.0
print(round(result, -2))  # 300.0
print(round(2.333333, 2))  # 2.33

# range()

my_range: range = range(1, 6)
print(my_range)  # range(1, 6)
print(list(my_range))  # [1, 2, 3, 4, 5]
another_range: range = range(0, 10, 2)  # 2 - step
print(list(another_range))  # [0, 2, 4, 6, 8]
negative_reversed_range: range = range(-5, 0)
print(list(negative_reversed_range))  # [-5, -4, -3, -2, -1]
negative_range: range = range(0, -5, -1)
print(list(negative_range))  # [0, -1, -2, -3, -4]

# slice()

numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers[2:4])  # [3, 4]
text: str = "Hello, world!"
first_three: slice = slice(0, 3)
print(text[first_three])  # Hel
reverse_slice: slice = slice(None, None, -1)  # [::-1]
print(text[reverse_slice])  # !dlrow ,olleH
step_two: slice = slice(None, None, 2)
print(text[step_two])  # Hlo ol!
