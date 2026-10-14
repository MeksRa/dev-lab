from typing import Final

MORSE_CODE_DICT: Final[dict[str, str]] = {
    # Latin alphabet (A-Z)
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    # Digits (0-9)
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    # Basic punctuation and spaces
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "/": "-..-.",
    " ": "/",
}

REVERSE_MORSE_DICT: Final[dict[str, str]] = {
    value: key for key, value in MORSE_CODE_DICT.items()
}


def text_to_morse(text: str) -> str:
    """Converts Text to Morse."""
    morse = [MORSE_CODE_DICT[i.upper()] for i in text if i.upper() in MORSE_CODE_DICT]
    return " ".join(morse)


def morse_to_text(morse: str) -> str:
    """Converts Morse to Text."""
    text = [REVERSE_MORSE_DICT.get(i, "") for i in morse.split(" ")]
    return "".join(text)


def is_morse_code(user_input: str) -> bool:
    """Checks whether the string is Morse code ( consists only of [.;-;/] )."""
    clean_input = user_input.replace(" ", "")
    morse_symbols = {".", "-", "/"}
    return all(i in morse_symbols for i in clean_input)


def main() -> None:

    print("\n======================= Morse Code Converter =======================")
    print("Enter text or Morse code (e.g., 'Hello' or '.... . .-.. .-.. ---').")
    print("Type 'exit' or 'quit' to close the program.")
    print("====================================================================")
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("Exiting the program...")
                break

            if not user_input:
                continue

            if is_morse_code(user_input):
                print(f"[Text]: {morse_to_text(user_input)}")
            else:
                print(f"[Morse]: {text_to_morse(user_input)}")
        except KeyboardInterrupt:
            print("Exiting the program...")
            break


if __name__ == "__main__":
    main()
