fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 1: apple
# 2: banana
# 3: orange

# ====================
tasks = ["Code Python", "Code Python", "Code Python", "Sleep"]

for index, task in enumerate(tasks, start=1):
    print(f"Task #{index} -> {task}")

# Task #1 -> Code Python
# Task #2 -> Code Python
# Task #3 -> Code Python
# Task #4 -> Sleep

# ====================
players = ["Alex", "John", "Kate", "Max"]

for index, name in enumerate(players):
    if name == "Kate":
        print(f"Kate is at index {index}")

# Kate is at index 2

# ====================
names = ["Falcon", "Apollo"]
print(list(enumerate(names)))

# [(0, 'Falcon'), (1, 'Apollo')]

# ====================
for index, letter in enumerate("Python"):
    print(index, letter)

# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

# ====================
numbers = [10, 20, 30]
for index, val in enumerate(numbers):
    numbers[index] = val * 2
print(numbers)

# [20, 40, 60]
