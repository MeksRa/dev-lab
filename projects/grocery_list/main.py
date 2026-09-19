# =================================
# 1) The first version
# =================================


def add_items(groceries: list[str]):
    add_grocery = input("What item would you like to add?: ")
    print(f'"{add_grocery}" has been added!')
    groceries.append(add_grocery)


def remove_items(groceries: list[str]):
    remove_grocery = input("What item would you like to remove?: ")
    if remove_grocery in groceries:
        print(f"{remove_grocery} has been removed!")
        groceries.remove(remove_grocery)
    else:
        print(f"{remove_grocery} hasn't been found in {groceries}")


def get_items(groceries: list[str]):
    while True:
        print("""Enter:
---------------------------
 1 - To add an item
 2 - To remove an item
 3 - To list all items
 0 - To exit the program
---------------------------""")
        user_input: str = input("Choose: ")
        if user_input == "0":
            print("Exiting program...")
            break
        elif user_input == "3":
            print("___LIST___")
            for grocery in groceries:
                print(f"- {grocery};")
            print("__________")
        elif user_input == "1":
            add_items(groceries)
        elif user_input == "2":
            remove_items(groceries)
        else:
            print("Invalid input. Try again.")


# def main() -> None:
#    groceries = []
#    print("Welcome to Groceries!")
#    get_items(groceries)

# if __name__ == "__main__":
#    main()


# =================================
# 02) The second version
# =================================


import sys


def welcome_message() -> None:
    print("""Welcome to Groceries!
    Enter:
    ---------------------------
     1 - To add an item
     2 - To remove an item
     3 - To list all items
     0 - To exit the program
    ---------------------------""")


def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f'"{item}" has been added!')


def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'"{item}" has been removed!')
    except ValueError:
        print(f'No "{item} found in: {groceries}')


def display(groceries: list[str]) -> None:
    print("___LIST___")
    for i, item in enumerate(groceries, 1):
        print(f"{i}: {item.capitalize()}")
    print("_" * 10)


def is_an_option(text: str) -> bool:
    return text in ["1", "2", "3", "0"]


def main() -> None:
    groceries: list[str] = []
    welcome_message()
    while True:
        user_input: str = input("Choose: ").lower()
        if not is_an_option(user_input):
            print("Please pick a valid option...")
            continue
        if user_input == "1":
            new_item: str = input("What item would you like to add? >>").lower()
            add_item(new_item, groceries)
        elif user_input == "2":
            item_to_removed: str = input(
                "What item would you like to remove? >>"
            ).lower()
            remove_item(item_to_removed, groceries)
        elif user_input == "3":
            display(groceries)
        elif user_input == "0":
            print("Exiting program...")
            sys.exit()


if __name__ == "__main__":
    main()
