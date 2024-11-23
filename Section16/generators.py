from typing import Generator


def five_numbers() -> Generator[int, None, None]:
    for i in range(5):
        yield i + 1


def huge_data() -> Generator[int, None, None]:
    for i in range(10_000_000_000):
        yield i


def main() -> None:
    numbers: Generator[int, None, None] = five_numbers()
    print(f"First number: {next(numbers)}")
    print(f"Second number: {next(numbers)}")
    print(f"Third number: {next(numbers)}")
    print(f"Fourth number: {next(numbers)}")
    print(f"Fifth number: {next(numbers)}")

    huge_numbers: Generator[int, None, None] = huge_data()
    for _ in range(5):
        print(f"\t{next(huge_numbers)}")


if __name__ == "__main__":
    main()
