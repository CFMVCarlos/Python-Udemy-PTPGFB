import math

if __name__ == "__main__":
    print("\n-->>print()")
    print("A", "B", "C", sep=" - ", end=" ***\n")
    print(*["Mario", "James", "Luigi"], sep=", ", end=".\n")

    print("\n-->>enumerate()")
    for i, v in enumerate(["Mario", "James", "Luigi"], start=1):
        print(i, v)

    print("\n-->>round()")
    print(math.pi * 100)
    print(round(math.pi * 100, 2))
    print(round(math.pi * 100, 0))
    print(round(math.pi * 100, -2))

    print("\n-->>range()")
    print(list(range(1, 51, 2)))
    print(list(range(0, -5, -1)))

    print("\n-->>slice()")
    text: str = "Hello, World!"
    first_three: slice = slice(0, 3)
    print(text[first_three])
    reversed: slice = slice(None, None, -1)
    print(text[reversed])
    step_two: slice = slice(None, None, 2)
    print(text[step_two])

    print("\n-->>globals()")
    print(globals())

    print("\n-->>locals()")
    print(locals())

    print("\n-->>all()")
    print(all([True, True, True]))
    print(all([True, False, True]))
    print(all([1, 1, 1, 0, 1, 0, 1, 1, 1, 0]))

    print("\n-->>any()")
    print(any([False, False, False]))
    print(any([True, False, False]))
    print(any([1, 1, 1, 0, 1, 0, 0, 0, 0, 0]))

    print("\n-->>isinstance()")
    print(isinstance(1, int))
    print(isinstance(1, float))
    print(isinstance(1, str))
    print(isinstance(1, (int, float)))
    print(isinstance(1, int | float))
