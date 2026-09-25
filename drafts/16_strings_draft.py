# ======================================================================== #

# text.capitalize()  # 'Hello world'
# text.title()  # 'Hello World'

# "Sam Harris".split()  # ['Sam', 'Harris']
# "apple,banana,orange".split(",")  # ['apple', 'banana', 'orange']

# "-".join(["2026", "09", "25"])  # '2026-09-25'
# "".join(["a", "b", "c"])  # 'abc'

# "ban" in "banjo"  # True
# "hello".find("e")  # 1 -> searches for the index of the first occurrence (returns -1 if not found)
# "hello".find("z")  # -1 ->

# .upper() / .lower() — change register
# name.lower().startswith("b")  # True

# .startswith()
# "photo.png".endswith(".png")


# "Hello World".replace("World", "Python")  # 'Hello Python'
# "a b c".replace(" ", "")  # 'abc'

# "  hello  ".strip()  # 'hello' -> remove empty spaces
# "  hello  ".lstrip()  # 'hello  '
# "  hello  ".rstrip()  # '  hello'

# "123".isdigit()  # True -> Only numbers
# "Hello".isalpha() # True -> Only letters
# "User123".isalnum() # True -> Only letters and numbers


def count_sheep(n: int) -> str:
    return "".join(f"{i} sheep..." for i in range(1, n + 1))


# print(count_sheep(5))


def are_you_playing_banjo_0(name: str) -> str:
    return (
        f"{name} plays banjo"
        if name[0].lower() == "r"
        else f"{name} does not play banjo"
    )


# print(are_you_playing_banjo_0("Rikke"))


def are_you_playing_banjo_1(name: str) -> str:
    return (
        f"{name} plays banjo"
        if name.lower().startswith("r")
        else f"{name} does not play banjo"
    )


# print(print(are_you_playing_banjo_1("Rikke")))

# ======================================================================== #
