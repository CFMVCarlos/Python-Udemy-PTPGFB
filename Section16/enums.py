from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1


class Color(Enum):
    RED = "R"
    GREEN = "G"
    BLUE = "B"


def buy_car(brand: str, color: Color) -> None:
    if color == Color.RED:
        print(f"Buying a {color.name} {brand} car.")
    elif color == Color.GREEN:
        print(f"Buying a {color.name} {brand} car.")
    elif color == Color.BLUE:
        print(f"Buying a {color.name} {brand} car.")
    else:
        print("Unknown color.")


def main() -> None:
    state: State = State.OFF
    if state == State.ON:
        print("The state is ON.")
    elif state == State.OFF:
        print("The state is OFF.")
    else:
        print("Unknown state.")

    print()

    red: Color = Color.RED
    print(red)
    print(red.name)
    print(red.value)
    print(Color("R"))

    print()

    buy_car("Toyota", Color.RED)
    buy_car("Honda", Color.GREEN)
    buy_car("BMW", Color.BLUE)


if __name__ == "__main__":
    main()
