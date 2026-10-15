import re
from collections import Counter


def get_text():
    try:
        with open("text.txt", "r") as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print("Error: 'text.txt' file not found. Please create it first.")
        return ""


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()

    words: list[str] = re.findall(r"\b\w+\b", lowered_text)

    word_counts: Counter = Counter(words)

    return word_counts.most_common()


def main() -> None:
    word_frequencies: list[tuple[str, int]] = []
    print("========= Word Frequency =========")
    while True:
        user_input = (
            input(
                "Do you want to read a file or write your own text?\n[Read/Write/Exit]: "
            )
            .strip()
            .lower()
        )
        if user_input == "exit":
            break

        if user_input in ["write", "w"]:
            text = input("Enter your text: ")
            word_frequencies: list[tuple[str, int]] = get_frequency(text)
        elif user_input in ["read", "r"]:
            word_frequencies: list[tuple[str, int]] = get_frequency(get_text())
            if not word_frequencies:
                continue
        else:
            print("Invalid Input. Available options: Read, Write, Exit.")
            continue

        print("--- -- ---\nWord frequencies:")
        for word, count in word_frequencies:
            print(f"{word}: {count}")
        print("--- -- ---")
    print("====================================")

if __name__ == "__main__":
    main()
