import sys


def welcome_message() -> None:
    print("Welcome to Groceries!")
    print("Enter:")
    print("------------------------")
    print("1 - To add an item")
    print("2 - To remove an item")
    print("3 - To list all items")
    print("4 - To change an item")
    print("0 - To exit the program")
    print("------------------------")


def add_item(item: str, groceries: list[str]) -> None:
    if not item:
        print("Item cannot be empty.")
        return
    groceries.append(item)
    print(f"'{item}' added to the list.")


def remove_item(item: str, groceries: list[str]) -> None:
    if not item:
        print("Item cannot be empty.")
        return
    if item not in groceries:
        print(f"'{item}' not found in the {groceries}.")
        return

    groceries.remove(item)
    print(f"'{item}' removed from the list.")


def change_item(index: int, item: str, groceries: list[str]) -> None:
    groceries[index - 1] = item
    print(f"Item at index {index} changed to '{item}'.")


def display(groceries: list[str]) -> None:
    print("___LIST___")
    for i, item in enumerate(groceries, 1):
        print(f"{i}. {item.capitalize()}")
    print("_" * 10)


def is_an_option(text: str) -> bool:
    return text in "01234"


def is_valid_index(index: str, groceries_size: int) -> bool:
    if not index.isdigit():
        print("Index must be a number.")
        return False

    if 1 <= int(index) <= groceries_size:
        return True

    print(f"Index out of range. Size is {groceries_size}.")
    return False


def main() -> None:
    groceries: list[str] = []

    welcome_message()
    while True:
        user_input: str = input("Enter an option: ").lower()
        if not is_an_option(user_input):
            print("Invalid option. Please try again.")
            continue

        if user_input == "0":
            print("Exiting the program...")
            sys.exit()

        if user_input == "1":
            item: str = input("What item to add? >> ").lower()
            add_item(item, groceries)
        elif user_input == "2":
            item: str = input("What item to remove? >> ").lower()
            remove_item(item, groceries)
        elif user_input == "3":
            display(groceries)
        elif user_input == "4":
            index: str = input("Enter the index: ").lower()
            if not is_valid_index(index, len(groceries)):
                continue
            item: str = input("Enter the new item: ").lower()
            change_item(int(index), item, groceries)


if __name__ == "__main__":
    main()
