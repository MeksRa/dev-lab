def calculate_split(total_amount: float, number_people: int) -> float:
    """Calculates the share of each person"""
    if number_people < 1:
        raise ValueError("Number of people must be at least 1.")

    return total_amount / number_people


def printer(
    currency: str, total_amount: float, number_people: int, share_per_person: float
) -> None:
    """Prints output"""
    print("=============================")
    print(f"Total expense: {currency}{total_amount:,.2f}")
    print(f"Number of people: {number_people}")
    print(f"Each person should pay: {currency}{share_per_person:,.2f}")
    print("=============================")


def main() -> None:
    """Entry point. Accepts input"""
    print("======= Bill Splitter =======")
    currency = "$"
    try:
        total_amount: float = float(input("Enter the total amount of the expense: "))
        number_people: int = int(
            input("Enter the number of people sharing the expense: ")
        )

        share_per_person = calculate_split(total_amount, number_people)
        printer(currency, total_amount, number_people, share_per_person)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
