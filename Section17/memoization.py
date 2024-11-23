import time
from functools import cache


@cache
def count_vowels(text: str) -> int:
    print("Counting...")
    time.sleep(3)
    return sum(text.count(vowel) for vowel in "AEIOUaeiou")


def main() -> None:
    while True:
        user_input: str = input("Enter some text: ").lower()

        if user_input == "info":
            print(f"Bot: {count_vowels.cache_info()}")
        elif user_input == "clear":
            count_vowels.cache_clear()
            print("Bot: Cache cleared!")
        else:
            print(f"Bot: The text has {count_vowels(user_input)} vowels.")


if __name__ == "__main__":
    main()