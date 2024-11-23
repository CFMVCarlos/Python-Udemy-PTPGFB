import time
from datetime import datetime


def greet(name: str, language: str, default: str = "Hello") -> None:
    if language == "it":
        print(f"Ciao, {name}!")
    else:
        print(f"{default}, {name}!")


def show_time() -> None:
    now: datetime = datetime.now()
    print(f"Time: {now:%H:%M:%S}")


def get_length(text: str) -> int:
    return len(text)

def make_upper(text: str) -> str:
    return text.upper()

def connect_to_internet(signal: bool, delay: int) -> None:
    if delay > 2:
        signal = True

    if signal:
        print("Connected!")
    else:
        print(f"Connection failed. Try again in {delay} seconds.")
        time.sleep(delay)
        connect_to_internet(signal, delay + 1)

def add(*numbers: int) -> int:
    return sum(numbers)

def greet_all(greeting: str, *people: str, ending: str) -> None:
    for person in people:
        print(f"{greeting}, {person}! {ending}")

def pin_position(*args, **kwargs: int) -> None:
    print(args)
    print(kwargs)

def special_parameters(var_a: str, / , var_b: str, *, var_c: str) -> None:
    print(var_a, var_b, var_c)

greet("Mario", "it")
show_time()
print(f"Length: {get_length("Python")}")
print(f"Upper: {make_upper("Python")}")
connect_to_internet(False, 1)
print(f"Sum: {add(1, 2, 3, 4)}")
greet_all("Hello", "Alice", "Bob", "Charlie", ending="Have a nice day!")
pin_position('a', 'b','c', x=10, y=20, z=30)
special_parameters('a', var_b='b', var_c='c')
special_parameters('a', 'b', var_c='c')



