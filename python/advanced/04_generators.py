from collections.abc import Generator

# --------------------------------


def five_numbers() -> Generator:
    yield from range(1, 6)

    # for i in range(1, 6):
    #     yield i


# generators are exhaustive
# once we retrieve a value
# it dissapears from that generator

numbers: Generator = five_numbers()
print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
print(list(numbers))  # [4, 5]
print(list(numbers))  # []

# --------------------------------

# It's incredibly memore efficient to use generators here


def huge_data() -> Generator:
    yield from range(1, 100_000_000_000)


# ------------


def generate_vowels() -> Generator:
    vowels: str = "aeiou"
    yield from vowels

    # for vowel in vowels:
    #     yield vowel


def main() -> None:
    data: Generator = huge_data()
    print(next(data))  # 1
    for i in range(200):
        print(next(data))  # 2-201

    # ------------

    vowels: Generator = generate_vowels()  # iterable
    print(next(vowels))  # a
    print(next(vowels))  # e
    print(next(vowels))  # i
    for vowel in vowels:
        print(vowel)  # a  # e  # i  # o  # u

    try:
        print(next(vowels))  # o
        print(next(vowels))  # u
        print(next(vowels))  # The generator is empty!
    except StopIteration:
        print("The generator is empty!")


if __name__ == "__main__":
    main()
