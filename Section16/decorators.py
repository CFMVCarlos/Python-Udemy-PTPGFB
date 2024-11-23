import time
from functools import wraps
from typing import Any, Callable


def get_time(func: Callable) -> Callable:
    """Times how long it takes to execute a function."""

    @wraps(func)  # This is used to preserve the metadata of the original function
    def wrapper(*args, **kwargs) -> None:
        start_time: float = time.perf_counter()
        func(*args, **kwargs)
        end_time: float = time.perf_counter()
        print(f"[wrapper]Execution time: {end_time - start_time: .3f}s")

    return wrapper


@get_time
def calculate() -> None:
    """Calculate() docstring."""

    print("[calculate]Calculating...")
    for i in range(20_000_000):
        pass
    print("[calculate]Done!")


def repeat(number: int) -> Callable:
    """Repeats a function a given number of times."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            value: Any = None
            for _ in range(number):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@repeat(number=3)
def greet(name: str) -> int:
    """Greets a person."""
    print(f"[greet]Hello, {name}!")
    return 100


def main() -> None:
    print(f"[main]{calculate.__name__}")
    print(f"[main]{calculate.__doc__}")
    calculate()

    print()

    value: int = greet("Alice")
    print(f"[main]Value: {value}")
    print(f"[main]{greet.__name__}")
    print(f"[main]{greet.__doc__}")


if __name__ == "__main__":
    main()
