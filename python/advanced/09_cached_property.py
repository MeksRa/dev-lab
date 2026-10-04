# let's do the same thing as decorator @cache but in classes

import time
from functools import cached_property


class DataSet:
    def __init__(self, data: list[float]) -> None:
        self._data = data

    def show_data(self) -> None:
        print(self._data)

    # using cache takes memory
    @cached_property  # a way to speed up func creating and using cache
    def sum(self) -> float:
        print("Calculating sum...")
        time.sleep(2)  # simulating high expensive func
        return sum(self._data)

    # using cache takes memory
    @cached_property  # a way to speed up func creating and using cache
    def mean(self) -> float:
        print("Calculating mean...")
        time.sleep(2)  # simulating high expensive func
        return sum(self._data) / len(self._data)


def main() -> None:
    ds: DataSet = DataSet([1.5, 2.5, 10, 7])
    ds.show_data()  # [1.5, 2.5, 10, 7]

    while True:
        user_input: str = input("You: ")

        if user_input == "clear sum":
            # it's better to use try/except for all the 'del' here
            del ds.sum
            print("Sum cache cleared!")
        elif user_input == "clear mean":
            del ds.mean
            print("Mean cache cleared!")
        elif user_input == "sum":
            print(ds.sum)
        elif user_input == "mean":
            print(ds.mean)
        else:
            print("Unknown command...")


if __name__ == "__main__":
    main()


# Output:
# [1.5, 2.5, 10, 7]
# You: sum
# Calculating sum...
# 21.0
# You: sum
# 21.0
# You: clear sum
# Sum cache cleared!
# You: sum
# Calculating sum...
# 21.0
# You: mean
# Calculating mean...
# 5.25
# You: mean
# 5.25
