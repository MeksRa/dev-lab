from random import choice


def play(attempts: int, word: str) -> None:
    """Game logic"""
    letters: str = ""
    while attempts > 0:
        if printer(word, letters) == 0:
            print("You got it!")
            break

        letter: str = input("Enter a letter: ").lower().strip()

        if not letter or len(letter) > 1 or not letter.isalpha():
            print("Try another letter!")
            continue

        if letter in letters:
            print(f"You already used: {letter}. Try another letter!")
            continue

        letters += letter

        if letter not in word:
            attempts -= 1
            print(f"That was wrong! ({attempts} attempts remaining)")

            if attempts == 0:
                printer(word, letters)
                print(f"No more attempts remaining. You lose. The word was: {word}")
                break


def printer(word: str, letters: str) -> int:
    """Prints UX"""
    blanks: int = 0
    print("Word: ", end="")
    for char in word:
        if char in letters:
            print(char, end="")
        else:
            print("_", end="")
            blanks += 1
    print()
    return blanks


def play_again() -> bool:
    """Asks the user if he wants to play another round"""
    while True:
        response = input("\nDo you want to play again? (y/n): ").strip().lower()
        if response in ("y", "yes"):
            return True
        if response in ("n", "no"):
            return False
        print("Please enter 'y' for yes or 'n' for no.")


def main() -> None:
    """Entry point."""
    words: list[str] = [
        "Secret",
        "GitHub",
        "MeksRa",
        "Keyboard",
        "Screen",
        "Router",
        "Hangman",
        "Internet",
        "Repository",
        "Python",
        "Mouse",
        "Steam",
        "Storage",
        "Laptop",
    ]
    name = input("What is your name? ").strip() or "Player"
    print(f"Welcome to Hangman, {name}!")
    while True:
        try:
            attempts: int = int(input(f"{name}, how many attempts do you need? "))
            if attempts <= 0:
                print(f"{name}, the number of attempts must be greater than 0")
                continue
        except ValueError:
            print(f"{name}, the number of attempts must be a digit.")
            continue

        word: str = choice(words).lower()
        play(attempts, word)
        if not play_again():
            print(f"Thanks for playing, {name}!")
            break


if __name__ == "__main__":
    main()
