from dataclasses import dataclass
from typing import Self


@dataclass
class Book:
    title: str
    author: str
    total_pages: int

    _current_page: int = 0  # encapsulated current page

    @property
    def current_page(self) -> int:
        """Gets current page"""
        return self._current_page

    @current_page.setter
    def current_page(self, page: int) -> None:
        """Sets current page. (Should be between 0 - max)"""
        if not (0 <= page <= self.total_pages):
            raise ValueError(f"Page should be from 0 to {self.total_pages}")

    @staticmethod
    def calculate_progress(current: int, total: int) -> float:
        """Calcucate percent of reading"""
        return round((current / total) * 100, 1)

    @classmethod
    def from_string(cls, book_str: str) -> Self:
        """Create an object from string 'Title | Author | Pages'"""
        parts = [p.strip() for p in book_str.split("|")]
        if len(parts) != 3:
            raise ValueError("Invalid string format. Use 'Title | Author | Pages'")
        return cls(title=parts[0], author=parts[1], total_pages=int(parts[2]))

    def __str__(self) -> str:
        progress = self.calculate_progress(self._current_page, self.total_pages)
        return f"'{self.title}' - {self.author} (Progress: {progress}%)"


class Library:
    def __init__(self, name: str) -> None:
        self.name = name
        self._books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add book to list 'self._books'"""
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        """Remove book from list 'self._books'"""
        self._books = [item for item in self._books if item.title != book.title]

    def find_by_author(self, author_name: str) -> list[Book]:
        """Returns a list of the current author's books"""
        return [
            book for book in self._books if book.author.lower() == author_name.lower()
        ]

    def get_all_books(self) -> list[Book]:
        """Returns a list of all books"""
        return self._books

    @classmethod
    def create_classic_library(cls) -> Self:
        """Fabric method: creates classic library"""
        lib = cls("Classic Library")
        lib.add_book(Book("Some_book", "Some_author", 1300))
        lib.add_book(Book("Some_book_2", "Some_author_2", 1230))
        return lib

    @property
    def book_count(self) -> int:
        """Count books in a list"""
        return len(self._books)

    @staticmethod
    def format_library_info(library: "Library") -> str:
        """Returns fomatted library"""
        lines = [f"Library: {library.name} (Books: {library.book_count})"]
        for book in library.get_all_books():
            lines.append(f"{book}")
        return "\n".join(lines)


class LibraryManager:
    def __init__(self) -> None:
        self._libraries: list[Library] = []

    def add_library(self, library: Library) -> None:
        """Add new library"""
        self._libraries.append(library)

    def get_libraries(self) -> list[Library]:
        """Get all libraries"""
        return self._libraries


def main() -> None:
    book1 = Book("Book1", "Author1", 100)
    book2 = Book("Book2", "Author2", 200)
    book3 = Book.from_string("Unknown_book | Unknown_author | 1579")

    library1 = Library("Library1")
    classic_lib = Library.create_classic_library()

    library1.add_book(book1)
    library1.add_book(book2)
    classic_lib.add_book(book3)

    lib_manager = LibraryManager()
    lib_manager.add_library(library1)
    lib_manager.add_library(classic_lib)

    for library in lib_manager.get_libraries():
        print(Library.format_library_info(library))


if __name__ == "__main__":
    main()

# OUTPUT:
# Library: Library1 (Books: 2)
# 'Book1' - Author1 (Progress: 0.0%)
# 'Book2' - Author2 (Progress: 0.0%)
# Library: Classic Library (Books: 3)
# 'Some_book' - Some_author (Progress: 0.0%)
# 'Some_book_2' - Some_author_2 (Progress: 0.0%)
# 'Unknown_book' - Unknown_author (Progress: 0.0%)
