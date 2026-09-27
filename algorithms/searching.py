def binary_search(arr: list[int], item: int) -> int | None:
    """Searches for the index of element "item" in an array "arr" sorted in ascending order.

    Complexity: O(log n)
    Returns the index of the element, or "None" if the element is not found.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    print(f"Index of 9: {binary_search(numbers, 9)}")  # 4
    print(f"Index of 2: {binary_search(numbers, 2)}")  # None
