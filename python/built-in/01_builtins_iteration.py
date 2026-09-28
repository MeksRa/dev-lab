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
