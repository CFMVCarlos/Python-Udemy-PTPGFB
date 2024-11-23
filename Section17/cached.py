import time
from functools import cached_property


class DataSet:
    def __init__(self, data: list[float]) -> None:
        self._data: list[float] = data

    def show_data(self) -> None:
        print(self._data)

    @cached_property
    def sum_data(self) -> float:
        print("Calculating sum...")
        time.sleep(2)
        return sum(self._data)

    @cached_property
    def mean_data(self) -> float:
        print("Calculating mean...")
        time.sleep(2)
        return sum(self._data) / len(self._data)


def main() -> None:
    ds: DataSet = DataSet([1.5, 2.5, 10, 7])
    ds.show_data()

    while True:
        user_input: str = input("You: ").lower()

        if user_input == "clear sum":
            try:
                del ds.sum_data
                print("Bot: Sum cache cleared!")
            except AttributeError:
                print("Bot: Sum cache is already cleared!")
        elif user_input == "clear mean":
            try:
                del ds.mean_data
                print("Bot: Mean cache cleared!")
            except AttributeError:
                print("Bot: Mean cache is already cleared!")
        elif user_input == "sum":
            print(f"Bot: The sum of the data is {ds.sum_data}.")
        elif user_input == "mean":
            print(f"Bot: The mean of the data is {ds.mean_data}.")
        else:
            print("Bot: I don't understand.")


if __name__ == "__main__":
    main()
