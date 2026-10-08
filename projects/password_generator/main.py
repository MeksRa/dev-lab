import secrets
import string


def contains_upper(password: str) -> bool:
    """Checks whether any letter satisfies the condition. (looks for uppercase)"""
    return any(char.isupper() for char in password)


def contains_symbols(password: str) -> bool:
    """Checks whether any letter satisfies the condition. (looks for symbols)"""
    return any(char in string.punctuation for char in password)


def contains_digits(password: str) -> bool:
    """Checks whether any letter satisfies the condition. (looks for digits)"""
    return any(char.isdigit() for char in password)


def generate_password(
    length: int, min_upper: int = 1, min_symb: int = 1, min_digits: int = 1
) -> str:
    """Generates Password.
    Concatenates Lowercase + Digits + Punctuation + Uppercase,
    creating a basis for generation."""

    # req_length = min_up + min_sy + min_ di
    # if length < req_length => length = req_length
    length = max(length, min_upper + min_symb + min_digits)

    base = (
        string.ascii_lowercase
        + string.digits
        + string.punctuation
        + string.ascii_uppercase
    )
    pass_chars = []

    # Guarantees minimum requirements
    for _ in range(min_upper):
        pass_chars.append(secrets.choice(string.ascii_uppercase))
    for _ in range(min_symb):
        pass_chars.append(secrets.choice(string.punctuation))
    for _ in range(min_digits):
        pass_chars.append(secrets.choice(string.digits))

    # Appends other chars
    while len(pass_chars) < length:
        pass_chars.append(secrets.choice(base))

    # Finally shuffles everything in the list
    secrets.SystemRandom().shuffle(pass_chars)
    return "".join(pass_chars)


def main() -> None:
    """Entry point. Password config. (len/uppers/symbs/digits)"""
    for i in range(1, 6):
        new_pass: str = generate_password(
            length=16, min_upper=2, min_symb=2, min_digits=3
        )
        specs = f"U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}, D: {contains_digits(new_pass)}"
        print(f"{i} -> {new_pass} ({specs})")


if __name__ == "__main__":
    main()
