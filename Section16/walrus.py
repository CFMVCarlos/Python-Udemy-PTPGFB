def description(numbers: list[int]) -> dict[str, float | int]:
    n_length: int = len(numbers)
    n_sum: int = sum(numbers)
    n_mean: float = n_sum / n_length

    details: dict[str, float | int] = {"length": n_length, "sum": n_sum, "mean": n_mean}
    return details


def description_walrus(numbers: list[int]) -> dict[str, float | int]:
    details: dict[str, float | int] = {
        "length": (n_length := len(numbers)),
        "sum": (n_sum := sum(numbers)),
        "mean": n_sum / n_length,
    }
    return details


def main() -> None:
    numbers: list[int] = [1, 10, 5, 200, -4, 7]
    print(description(numbers))
    print(description_walrus(numbers))

    print()

    items: dict[int, str] = {1: "Cup", 2: "Chair"}
    if item := items.get(3):
        print(f"You have the item: {item}")
    else:
        print("Item not found!")


if __name__ == "__main__":
    main()
