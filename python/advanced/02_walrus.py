# := Walrus Operator. (Python 3.8+)


def description(numbers: list[int]) -> dict:

    details: dict = {
        "length": (n_length := len(numbers)),
        "sum": (n_sum := sum(numbers)),
        "mean": n_sum / n_length,
    }
    return details


def main() -> None:
    numbers: list[int] = [1, 10, 5, 200, -4, 7]
    print(description(numbers))  # {'length': 6, 'sum': 219, 'mean': 36.5}
    # =====
    print(x := 1 > 0)  # True  # noqa: PLR0133
    print(x)  # True
    # =====
    items: dict[int, str] = {1: "Cup", 2: "Chair"}
    if item := items.get(3):  # means if item is None this block will be failed
        print(f"You have: {item}")
    else:
        print("No item found...")


if __name__ == "__main__":
    main()
