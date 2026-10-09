import itertools
import string
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "words.txt"


def common_guess(word: str) -> str | None:
    # We can provide common_guess() with list with the most common words
    # to use it before brute force
    with DATA_FILE.open("r", encoding="utf-8") as file:
        word_list: list[str] = file.read().splitlines()

    for i, match in enumerate(word_list, start=1):
        if match == word:
            return f"Common match: {match} (#{i})"


def brute_force(
    word: str, length: int, digits: bool = False, symbols: bool = False
) -> str | None:
    chars: str = string.ascii_lowercase
    # more options = slower program
    if digits:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    attempts: int = 0
    for attempts, guess_tuple in enumerate(
        itertools.product(chars, repeat=length), start=1
    ):
        guess = "".join(guess_tuple)

        if guess == word:
            return f'"{word}" was cracked in {attempts:,} guesses.'

        # print(guess, attempts)  # 'print' takes too many resources


def main() -> None:
    print("Searching...")
    password: str = "bbbbb"
    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)
    else:
        for i in range(3, 6):
            if cracked := brute_force(password, length=i, digits=False, symbols=False):
                print(cracked)
                break
            else:
                print("There was no match")

    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), "s")


if __name__ == "__main__":
    main()
