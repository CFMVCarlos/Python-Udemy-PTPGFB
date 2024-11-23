from datetime import datetime
from random import choice


class ChatBot:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def get_description(self) -> str:
        return f"{self.name} is a bot who is {self.age} years old"

    def get_response(self, user_input: str) -> str:
        lowered: str = user_input.lower()
        if "hello" in lowered:
            return f"{self.name}: Hey there!"
        elif "bye" in lowered:
            return f"{self.name}: See you!"
        elif "how old" in lowered:
            return f"{self.name}: I am {self.age} years old"
        elif "time" in lowered:
            return f"{self.name}: The time is {datetime.now():%H:%M:%S}"
        elif "how are you" in lowered:
            return f"{self.name}: I'm doing well, thank you!"
        else:
            random_responses: list[str] = [
                "I don't understand",
                "Would you mind rephrasing that?",
                "What?",
                "Ah, what?",
            ]
            return f"{self.name}: {choice(random_responses)}"

    def run(self) -> None:
        while True:
            user_input: str = input("You: ")
            if user_input.lower() == "exit":
                print(f"{self.name}: Thanks for chatting with {self.name}!")
                break
            response: str = self.get_response(user_input)
            print(response)


if __name__ == "__main__":
    bot: ChatBot = ChatBot("PyBot", 27)
    print(bot.get_description())
    bot.run()
