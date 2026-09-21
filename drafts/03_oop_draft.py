class Task:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.is_done = False

    def mark_done(self) -> None:
        if self.is_done:
            print("Warning: The task is already completed!")
        else:
            self.is_done = True
            print(f'Task "{self.title}" is now marked as completed!')

    def update_description(self, new_description: str) -> None:
        if self.is_done:
            print("Error: Cannot change description of a completed task")
        else:
            self.description = new_description
            print(f"Done! New description: {new_description}")

    def update_title(self, new_title: str) -> None:
        if self.is_done:
            print("Error: Cannot change title of a completed task")
        else:
            self.title = new_title
            print(f"Done! New title: {new_title}")

    def get_info(self) -> None:
        if self.is_done:
            status = "Completed"
        else:
            status = "In progress"
        print(f"You actual task:\n{self.title}: {self.description}\nStatus: {status}")


def menu():
    print("Greetings! Enter the title and description of your first task!")

    task: Task = Task(input("Title: "), input("Description: "))

    while True:
        print("""
        -------------------
        Simple Task Tracker
        Options:
        [Show]
        [Complete]
        [Title]
        [Description]
        [Exit]
        -------------------
        """)

        user_input = input("You: ").lower()
        if "show" in user_input:
            task.get_info()
        elif "title" in user_input:
            task.update_title(input(f"Enter a new title for {task.title}: "))

        elif "description" in user_input:
            task.update_description(
                input(f"Enter a new description for {task.title} here: ")
            )

        elif "complete" in user_input:
            task.mark_done()

        elif "exit" in user_input:
            break
        else:
            print("Invalid input")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
