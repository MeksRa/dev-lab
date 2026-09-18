# just input without error checking
import sys


def just_input():
    total: int = 0
    while True:
        user_input: str = input("Enter a number: ")
        if user_input == "0":
            print("Total:", total)
            sys.exit()
        total += int(user_input)


# just_input()

# some shortcuts


# F2 => rename all selected words
def show_stats(name: str) -> None:
    print(f"{name} is a good name!")
    print(f"{name} is {len(name)} characters long.")
    print(f"{name} in uppercase is {name.upper()}")


show_stats("James")
