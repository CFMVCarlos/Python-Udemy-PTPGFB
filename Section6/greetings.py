from typing import Final

AUTHOR: Final[str] = "Carlos"
VERSION: Final[int] = 1


def greet(name: str) -> None:
    print(f"Hello, {name}!")
