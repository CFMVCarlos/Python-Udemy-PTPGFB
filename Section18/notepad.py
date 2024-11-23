import sys


class Notepad:
    def __init__(self, author: str, filename: str) -> None:
        self.author: str = author
        self._filename: str = filename

    def show_instructions(self) -> None:
        print(f"\nWelcome to Notepad, {self.author}!")
        print("Commands:")
        print("1 - write note")
        print("2 - display note")
        print("0 - exit NotePad")

    def _write_note(self) -> None:
        user_input: str = input("Enter your note: ")

        with open(self._filename, "w") as note:
            note.write(user_input)
        print("Bot: Note saved successfully!")

    def _display_note(self) -> None:
        try:
            with open(self._filename, "r") as note:
                text: str = note.read()
                print(f"Bot: {text}")
        except FileNotFoundError:
            print("Bot: You need to write a note first!")

    def _exit_notepad(self) -> None:
        print(f"See you next time, {self.author}!")
        sys.exit()

    def run(self) -> None:
        while True:
            self.show_instructions()
            user_choice: str = input(f"{self.author}: Enter your choice: ")

            if user_choice == "1":
                self._write_note()
            elif user_choice == "2":
                self._display_note()
            elif user_choice == "0":
                self._exit_notepad()
            else:
                print("Bot: Invalid choice. Please try again.")


def main() -> None:
    notepad: Notepad = Notepad("Mario", "Section18/note.txt")
    notepad.run()


if __name__ == "__main__":
    main()
