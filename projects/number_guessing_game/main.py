from random import randint


def get_input(prompt: str) -> int:
    """Safely prompts the user for an integer until valid input is given"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_range() -> tuple[int, int]:
    """Prompts for low and high bounds, ensuring low <= high."""
    while True:
        low_num = get_input("Enter lower bound: ")
        high_num = get_input("Enter upper bound: ")

        if low_num <= high_num:
            return low_num, high_num

        print("Lower bound cannot be greater than upper bound. Try again.")


def play_game() -> None:
    """Main game logic loop."""
    low_num, high_num = get_range()
    target_num = randint(low_num, high_num)

    print(f"\nGuess the number in the range from {low_num} to {high_num}.")

    attempts = 0
    while True:
        user_guess = get_input("Your guess: ")
        attempts += 1

        if user_guess > target_num:
            print(f"The number is lower than {user_guess}.")
        elif user_guess < target_num:
            print(f"The number is higher than {user_guess}.")
        else:
            print(f"You won! The correct number was {user_guess}. Attempts: {attempts}")
            break


def ask_play_again() -> bool:
    """Asks the user if they want to play another round"""
    while True:
        response = input("\nDo you want to play again? (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def main() -> None:
    """Program entry point"""
    print("Welcome to the Guess the Number Game!")
    while True:
        play_game()
        if not ask_play_again():
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
