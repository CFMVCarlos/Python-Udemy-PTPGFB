"""
This is a docstring for the basics module. This module contains some basic functions and variables to demonstrate the concept of modules in Python.
"""

import math


class User:
    """
    Represents a user.

    Attributes:
        name (str): The name of the user.
    """

    def __init__(self, user_id: int) -> None:
        self.user_id: int = user_id

    def show_id(self) -> int:
        """
        Returns the user's ID.

        Returns:
            int: The user's ID.
        """
        return self.user_id


def user_exists(user: User, database: set[User]) -> bool:
    """
    Checks if a user exists in the database.

    Args:
        user (User): The user to check.
        database (set[User]): The database to check.

    Returns:
        bool: True if the user exists in the database, False otherwise.
    """
    return user in database


if __name__ == "__main__":
    user: User = User(1)
    print(user.show_id())

    print()

    big_number: float = 123_456_789
    print(f"{big_number}")
    print(f"{big_number:,}")
    print(f"{big_number:_}")

    print()

    fraction: float = 1234.56789
    print(f"{fraction}")
    print(f"{fraction:.2f}")

    print()

    percent: float = 0.5
    print(f"{percent:.0%}")
    print(f"{percent:.2%}")

    print()

    var: str = "BOB"
    print(f"{var:10}: Hello")
    print(f"{var:>10}: Hello")
    print(f"{var:^10}: Hello")
    print(f"{var:_>10}")
    print(f"{var:*^10}")

    print()

    programming_language: str = "Python"
    path: str = (
        f"C:\\testes\\{programming_language}\\Udemy\\The Professional Guide For Beginners\\Section13\\basics.py"
    )
    print(path)
    path: str = (
        rf"C:\testes\{programming_language}\Udemy\The Professional Guide For Beginners\Section13\basics.py"
    )
    print(path)
