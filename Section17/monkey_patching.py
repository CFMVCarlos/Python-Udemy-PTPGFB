import logging
import time
from typing import Callable


class Internet:
    def __init__(self, provider: str) -> None:
        self.provider: str = provider

    def connect(self) -> None:
        print(f"[{self.provider}] Connecting...")
        time.sleep(2)
        print(f"[{self.provider}] You are now connected!")


def test_connect() -> None:
    print("[Provider] You are now connected!")


def new_print(text: str) -> None:
    logging.warning(text)


def main() -> None:
    internet: Internet = Internet("Verizon")
    internet.connect = test_connect  # Monkey patching
    internet.connect()

    print: Callable = new_print
    print("Hello, world!")
    print("This is a warning message.")


if __name__ == "__main__":
    main()
