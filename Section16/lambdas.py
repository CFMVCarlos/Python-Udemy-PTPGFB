from typing import Callable


def use_all(f: Callable, values: list[int]) -> None:
    max_value: int = max(values)*2+1
    for value in values:
        f(value*2+1, max_value)

def main() -> None:
    use_all(lambda v, max: print(f"{v * "X":^{max}}"), list(range(10)))


if __name__ == '__main__':
    main()
