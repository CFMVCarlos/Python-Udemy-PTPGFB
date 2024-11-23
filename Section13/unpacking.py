if __name__ == "__main__":
    # Normal way
    a = 5
    b = 10
    temp = a
    a = b
    b = temp
    print(a, b)

    # Pythonic way
    a, b = 5, 10
    a, b = b, a
    print(a, b)

    print()

    a, *b, c = [1, 2, 3, 4, 5]
    print(a)
    print(b)
    print(c)

    print()

    numbers: list[int] = [1, 2, 3, 4, 5]
    params: dict[str, str] = {"end": ".", "sep": "-"}
    print(*numbers, **params)  # type: ignore
