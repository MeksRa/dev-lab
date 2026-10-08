from random import randint


def get_input(prompt: str) -> int:
    """Safely gets user input until valid integer is given"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def get_dice(amount: int) -> list[int]:
    """Creates a list with numbers in range 1-6; list Length = amount"""
    return [randint(1, 6) for _ in range(amount)]


def play_again() -> bool:
    """Asks the user if they want to play another round"""
    while True:
        response = input("\nDo you want to play again? (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def main() -> None:
    """Entry point. asks what the user wants"""
    while True:
        dice_count = get_input("How many dice would you like to roll? ")
        dice_results = get_dice(dice_count)
        # map(str, dice_results)  # -> converts numbers into strings
        print(f"You rolled: {', '.join(map(str, dice_results))}")
        if not play_again():
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
