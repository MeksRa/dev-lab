import re
from collections import Counter
from pathlib import Path

FILE_NAME = "text.txt"


def open_file(path: Path) -> str:
    """Opens text file and returns the text content"""
    try:
        with open(path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{path.name}' not found.")
        return ""


def get_frequency(text: str) -> list[tuple[str, int]]:
    """Counts the most frequent words"""
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_text)
    word_counts: Counter = Counter(words)

    return word_counts.most_common()


def analyse(text: str) -> dict[str, int | list[tuple[str, int]]]:
    """Analyses any string and returns dictionary"""
    result: dict[str, int | list[tuple[str, int]]] = {
        "total_chars_incl_spaces": len(text),
        "total_chars_excl_spaces": len(text.replace(" ", "")),
        "total_spaces": text.count(" "),
        "total_words": len(text.split()),
        "word_frequencies": get_frequency(text),
    }
    return result


def printer(analysis: dict[str, int | list[tuple[str, int]]]) -> None:
    """Prints the information"""
    print("====================")
    for key, value in analysis.items():
        if key == "word_frequencies" and isinstance(value, list):
            print("====================\nWord Frequencies:")
            for word, count in value:
                print(f"{word}: {count}")

        else:
            print(f"{key}: {value}")
    print("====================")


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    file_path = script_dir / FILE_NAME

    text: str = open_file(file_path)
    if not text:
        return

    analysis: dict[str, int | list[tuple[str, int]]] = analyse(text)
    printer(analysis)


if __name__ == "__main__":
    main()
