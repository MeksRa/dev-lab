var: int = -5
# assert var > 0, f"{var} is not more than 0"  # AssertionError: -5 is not more than 0


def start_program(db: dict[int, str]) -> None:
    assert db, "Database is empty"  # only for debugging

    print("Loaded:", db)
    print("Program started successfully!")


def main() -> None:                         # Loaded: {0: 'a', 1: 'b'}
    db1: dict[int, str] = {0: "a", 1: "b"}  # Program started successfully!
    # db1: dict[int, str] = {}  # AssertionError: Database is empty
    start_program(db=db1)


if __name__ == "__main__":
    main()
