import sys
from datetime import datetime


def get_response(text: str) -> str:
    lowered: str = text.lower()
    if lowered in {"hello", "hi", "hey"}:
        return "Hey there!"
    if "how are you" in lowered:
        return "I'm good, thank you!"
    if "your name" in lowered:
        return "My name is: Bot :)"
    if "time" in lowered:
        return f"The time is: {datetime.now():%H:%M:%S}"
    if lowered in {"bye", "see you", "goodbye"}:
        return "It was nice talking to you! Goodbye!"
    return "I don't understand you."


while True:
    user_input: str = input("You: ")

    if user_input.lower() in {"quit", "exit"}:
        print("Bot: It was nice talking to you! Goodbye!")
        sys.exit()

    bot_response: str = get_response(user_input)
    print(f"Bot: {bot_response}")
