class Task:
    def __init__(self, title: str) -> None:
        self.title = title

        self.is_done = False

    def mark_as_done(self) -> None:
        self.is_done = True

    def __str__(self) -> str:
        status = "Done" if self.is_done else "In progress"
        return f"[{status}] {self.title}"


class TodoList:
    def __init__(self) -> None:

        self.tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        """Creates task, add to list and return it."""
        task = Task(title)
        self.tasks.append(task)
        return task

    def remove_task(self, index: int) -> bool:
        """Remove task by index"""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_tasks(self) -> list[Task]:
        """Returns all list"""
        return self.tasks


def main() -> None:
    my_todos = TodoList()

    my_todos.add_task("Learn Python")
    my_todos.add_task("Learn smth else")
    my_todos.add_task("Learn more")

    tasks = my_todos.get_tasks()
    tasks[0].mark_as_done()

    print("Tasks:")
    for i, task in enumerate(my_todos.get_tasks()):
        print(f"{i}. {task}")

    my_todos.remove_task(1)

    print("Tasks (after removing):")
    for i, task in enumerate(my_todos.get_tasks()):
        print(f"{i}. {task}")


if __name__ == "__main__":
    main()
