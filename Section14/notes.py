import stat
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Note:
    id: UUID = field(init=False)
    title: str
    body: str

    def __post_init__(self) -> None:
        self.id = uuid4()


class NoteApp:
    def __init__(self, author: str, notes: list[Note] | None = None) -> None:
        self.author: str = author

        if notes is None:
            self._notes: list[Note] = []
        else:
            self._notes = notes

        self.display_instructions()

    @staticmethod
    def display_instructions() -> None:
        print("Welcome to Notes!")
        print("Here are the commands:")
        print("1 - Add new note")
        print("2 - Edit note")
        print("3 - Delete note")
        print("4 - Display all notes")

    def _add_note(self) -> None:
        title: str = input("Title: ")
        body: str = input("Body: ")

        note: Note = Note(title, body)
        self._notes.append(note)
        print("Note added successfully!")

    def _edit_note(self) -> None:
        print("Which note would you like to edit?")
        self._show_notes()

        try:
            note_index: int = int(input("Index: ")) - 1
            current: Note = self._notes[note_index]

            new_title: str = input(f"New title: ")
            new_body: str = input(f"New body: ")

            current.title = new_title
            current.body = new_body
            print("Note edited successfully!")
        except IndexError:
            print("Please select a valid note index...")
            self._edit_note()
        except ValueError:
            print("Index cannot be empty...")
            print("Aborting...")

    def _delete_note(self) -> None:
        print("Which note would you like to delete?")
        self._show_notes()

        try:
            note_index: int = int(input("Index: ")) - 1
            current: Note = self._notes[note_index]

            self._notes.remove(current)
            print("Note deleted successfully!")
        except IndexError:
            print("Please select a valid note index...")
            self._delete_note()
        except ValueError:
            print("Index cannot be empty...")
            print("Aborting...")

    def _show_notes(self) -> None:
        if not self._notes:
            print("No notes found...")
            return

        for i, note in enumerate(self._notes, 1):
            print(f"[{i}] {note.title}: {note.body}")

    def _select_option(self, user_input: str) -> None:
        if user_input not in "1234":
            print("Invalid option...")
            return

        if user_input == "1":
            self._add_note()
        elif user_input == "2":
            self._edit_note()
        elif user_input == "3":
            self._delete_note()
        elif user_input == "4":
            self._show_notes()

    def run_app(self) -> None:
        while True:
            user_input: str = input("You: ")
            self._select_option(user_input)


if __name__ == "__main__":
    note: Note = Note("Hello", "My name is Bob.")
    print(note)

    sample_notes: list[Note] = [
        Note(title="Title1", body="Hello there, Bob!"),
        Note(title="Title2", body="More text!"),
    ]

    note_app: NoteApp = NoteApp(author="Bob", notes=sample_notes)
    note_app.run_app()
