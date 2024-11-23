if __name__ == "__main__":
    print("\n-->>callable()")
    print(callable(print))
    print(callable(lambda x: x))
    print(callable(5))

    print("\n-->>filter()")
    numbers: list[int] = list(range(21))
    evens: list[int] = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)
    evens_comp: list[int] = [x for x in numbers if x % 2 == 0]
    print(evens_comp)

    print("\n-->>map()")
    squares: list[int] = list(map(lambda x: x**2, numbers))
    print(squares)
    squares_comp: list[int] = [x**2 for x in numbers]
    print(squares_comp)

    print("\n-->>sorted()")
    print(sorted(numbers))
    print(sorted(numbers, reverse=True))
    print(sorted(numbers, key=lambda x: x % 5))

    print("\n-->>eval()")
    print(eval("5 + 3"))
    print(eval("numbers[:5]"))

    print("\n-->>exec()")
    exec("print('Hello, World!')")

    print("\n-->>zip()")
    index: list[int] = list(range(1, 5))
    names: list[str] = ["Alice", "Bob", "Charlie"]
    ages: list[int] = [25, 30, 35, 9999]
    people: list[tuple[int, str, int]] = list(zip(index, names, ages))
    print(people)
