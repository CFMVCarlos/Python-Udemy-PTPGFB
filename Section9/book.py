class Book:
    def __init__(self, title: str, pages: int) -> None:
        self.title: str = title
        self.pages: int = pages

    def __len__(self) -> int:
        return self.pages

    def __add__(self, other: "Book") -> "Book":
        combined_title: str = f"{self.title} & {other.title}"
        combined_pages: int = self.pages + other.pages
        return Book(combined_title, combined_pages)


if __name__ == "__main__":
    py_daily: Book = Book("PyDaily", 100)
    harry_potter: Book = Book("Harry Potter", 340)
    print(len(py_daily))
    print(len(harry_potter))

    print()

    combined_book: Book = py_daily + harry_potter
    print(combined_book.title)
    print(len(combined_book))
