from dataclasses import dataclass


@dataclass
class MediaItem:
    id: int
    title: str
    year: int
    is_completed: bool = False

    def __str__(self) -> str:
        return f"id: {self.id} | Title: {self.title} | Year: {self.year} | Completed: {self.is_completed}"


class Library:
    def __init__(self) -> None:
        self.items: list[MediaItem] = []

    def add_item(self, item: MediaItem) -> None:
        self.items.append(item)

    def remove_item(self, item_id: int) -> None:
        self.items = [item for item in self.items if item.id != item_id]

    def show_items(self) -> None:
        if not self.items:
            print("Empty")
            return
        for item in self.items:
            print(item)


def main() -> None:
    my_library = Library()
    # ---
    book_1 = MediaItem(1, "Python OOP", 1312)
    book_2 = MediaItem(2, "Clear Code", 1583, is_completed=True)
    # ---
    my_library.add_item(book_1)
    my_library.add_item(book_2)
    # ---
    print("Before removing item with id 1")
    my_library.show_items()
    my_library.remove_item(1)
    print("After removing item with id 1")
    my_library.show_items()
    # ---


if __name__ == "__main__":
    main()
