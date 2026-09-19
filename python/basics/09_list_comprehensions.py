def first_lc():
    numbers: list[int] = [1, 2, 3]
    doubled: list[int] = []

    for number in numbers:
        doubled.append(number * 2)
    print(doubled)  # [2, 4, 6]

    doubled_lc: list[int] = [number * 2 for number in numbers]  # LC
    # "number * 2" => element that we want to return,
    # the for loop that we wanna use
    print(doubled_lc)  # [2, 4, 6]


# first_lc()


def second_lc():
    names: list[str] = ["Mario", "James", "Luigi", "John"]
    j_names: list[str] = []

    for name in names:
        if name.startswith("J"):
            j_names.append(name)
    print(j_names)

    j_names_lc: list[str] = [name for name in names if name.startswith("J")]  # LC
    # "name" => element that we want to return,
    # "for name in names" => the for loop that we wanna use,
    # "if name.startswith("J")" => condition
    print(j_names_lc)  # ['James', 'John']


# second_lc()


def third_lc():
    numbers: list[int] = [1, 2, 4, 6, 7, 10]
    even_numbers: list[int] = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print(even_numbers)

    even_numbers_lc: list[int] = [number for number in numbers if number % 2 == 0]  # LC
    print(even_numbers_lc)


# third_lc()
