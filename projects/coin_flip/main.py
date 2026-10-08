from random import choice


def flip_coin() -> str:
    return choice(["Heads", "Tails"])


def main() -> None:
    """Entry point for Coin Flip game. [ Heads or Tails ]"""
    print("Welcome to the Coin Flip Game!")
    while True:
        print("Heads or Tails?")
        user_input = input('Press Enter or type "exit" to quit: ').strip().lower()
        if user_input == "exit":
            print("Thanks for playing!")
            break
        print(f"|=============|\n|Result: {flip_coin()}|\n|=============|")


if __name__ == "__main__":
    main()
