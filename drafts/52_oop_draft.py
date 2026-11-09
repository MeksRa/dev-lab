from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    total_pages: int

    _current_page: int = 0  # encapsulated current page

    @property
    def current_page(self) -> int:
        return self._current_page

    @current_page.setter
    def current_page(self, page: int) -> None:
        if not (1 <= page <= self.total_pages):
            raise ValueError(f"Page should be from 1 to {self.total_pages}")

    # for calculation percent of reading
    @staticmethod
    def calculate_progress(current: int, total: int) -> float:
        return round((current / total) * 100, 1)

    def __str__(self) -> str:
        progress = self.calculate_progress(self._current_page, self.total_pages)
        return f"'{self.title}' - {self.author} (Progress: {progress}%)"


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        self._books = [item for item in self._books if item.title != book.title]

    def find_by_author(self, author_name: str) -> list[Book]:
        """Returns a list of the current author's books"""
        return [
            book for book in self._books if book.author.lower() == author_name.lower()
        ]

    def get_all_books(self) -> list[Book]:
        return self._books

    @property
    def book_count(self) -> int:
        return len(self._books)

    @staticmethod
    def format_library_info(library: "Library") -> str:
        lines = [f"Library: {library.name} (Books: {library.book_count})"]
        for book in library.get_all_books():
            lines.append(f"{book}")
        return "\n".join(lines)


class LibraryManager:
    def __init__(self) -> None:
        self._libraries: list[Library] = []

    def add_library(self, library: Library) -> None:
        self._libraries.append(library)

    def get_libraries(self) -> list[Library]:
        return self._libraries

def main() -> None:
    book1 = Book("Book1", "Author1", 100)
    book2 = Book("Book2", "Author2", 200)

    library1 = Library("Library1")
    library1.add_book(book1)
    library1.add_book(book2)

    lib_manager = LibraryManager()
    lib_manager.add_library(library1)

    for library in lib_manager.get_libraries():
        print(Library.format_library_info(library))


if __name__ == "__main__":
    main()