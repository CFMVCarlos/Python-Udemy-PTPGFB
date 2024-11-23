import sys
from typing import NoReturn


def sum_numbers() -> NoReturn:
    total: float = 0
    while True:
        user_input: str = input("Enter a number: ")

        if user_input == "0":
            print("Total: ", total)
            sys.exit(0)

        try:
            total += float(user_input)
        except ValueError:
            print("Invalid input")


def error_handling() -> None:
    try:
        result: float = 10 / 0
        print(result)
    except Exception as e:
        print("Error: ", e)

    print("Done")


def user_input() -> NoReturn:
    while True:
        try:
            user_input: str = input("Enter a number: ")
            print(f"10 / {user_input} = {10 / int(user_input)}")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print("Error: ", e)


def complex_error_handling() -> None:
    user_input: str = "0"

    try:
        result: float = 1 / float(user_input)
        print(f"1/{user_input} = {result}")
    except ValueError:
        print(f'You cannot use: "{user_input}" as value')
    except ZeroDivisionError:
        print("Don't be silly, you cannot divide by zero")
    else:
        print("No errors occurred")
    finally:
        print("This will always execute")


def check_age(age: int) -> bool:
    if age < 0:
        raise ValueError("Not a valid age...")

    if age >= 21:
        print("You are old enough")
        return True

    print("You are not old enough...")
    return False


def main() -> NoReturn | None:
    # sum_numbers()
    # error_handling()
    # user_input()
    # complex_error_handling()
    check_age(-10)


if __name__ == "__main__":
    main()
