class Ereader:
    def __init__(self, title: str, total_pages: int) -> None:
        # unique attributes
        self.title: str = title
        self.total_pages: int = total_pages
        # general attributes
        self.current_page: int = 1
        self.battery_level: int = 100

    def read_pages(self, pages_count: int) -> None:
        if self.battery_level == 0:  # Guard Clause
            print("Error: Battery is dead! Please recharge.")
            return  # 1
        if pages_count <= 0:  # Guard Clause
            print("Error: Invalid pages count!")
            return  # 2

        self.current_page += pages_count
        self.current_page = min(self.current_page, self.total_pages)

        print(
            f"Read {pages_count} pages. Now at page {self.current_page}/{self.total_pages}."
        )

        self.battery_level -= pages_count // 10

        self.battery_level = max(self.battery_level, 0)

    def charge(self) -> None:
        if self.battery_level == 100:  # Guard Clause
            print("Battery is already full!")
            return  # 1
        self.battery_level = 100
        print("Device fully charged to 100")

    def __str__(self) -> str:
        return f"Book: {self.title} | Page: {self.current_page}/{self.total_pages} | Battery: {self.battery_level}%/100%"


def menu():
    book1: Ereader = Ereader("Harry Potter", 500)
    print(book1.title, book1.total_pages)
    while True:
        print(
            "-_---___-\n[0] <- Exit, [1] <- Charge, [2] <- Read Pages, [3] <- Info\n-___---_-"
        )
        user_input = input("BookLover: ")
        if "0" == user_input:
            break
        elif "1" == user_input:
            book1.charge()
        elif "2" == user_input:
            pages_input = input("How many pages do you wanna read? ").strip()
            if not pages_input.isdigit():
                print("Error: Please enter a valid positive number.")
            else:
                book1.read_pages(int(pages_input))
        elif "3" == user_input:
            print(book1)
        else:
            print("Invalid input.")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
