from collections.abc import Callable

# -----------------

# x -> parameter that lambda should use,
# after ":" u insert a line of code that u want to execute
p = lambda x: print(x)  # PEP8 says u shouldn't store lambda functions in variables.
p("Hello")  # Hello

add = lambda a, b: a + b  # PEP8 says u shouldn't store lambda functions in variables.
print(add(5, 11))  # 16

# -----------------


def use_all(f: Callable[[int], None], values: list[int]) -> None:
    for value in values:
        f(value)


use_all(lambda v: print(f"{v * 'X'}"), [2, 4, 10])  # one-time lambda func

# XX
# XXXX
# XXXXXXXXXX


def multiply_x(value: int) -> None:  # Reusable, good practice
    print(f"{value * 'X'}")


use_all(multiply_x, [2, 4, 10])


# XX
# XXXX
# XXXXXXXXXX

# -----------------

# The best way to use lambda func
users = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_users = sorted(users, key=lambda user: user[1])
# sort a list of tuples by the second element

# -----------------

names: list[str] = ["Bob", "James", "Samantha", "Luigi", "Joe"]
sorted_names: list[str] = sorted(names)
print(sorted_names)
# ['Bob', 'James', 'Joe', 'Luigi', 'Samantha']

# default sort -> alphabetical(ascii order)
# Let's switch to sorting by length

sorted_names: list[str] = sorted(names, key=lambda x: len(x))
print(sorted_names)
# ['Bob', 'Joe', 'James', 'Luigi', 'Samantha']

# -----------------
