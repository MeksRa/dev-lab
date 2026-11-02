class Task:
    def __init__(self, title: str) -> None:
        self.title = title
        self.is_done = False

    def toggle(self) -> None:
        self.is_done = not self.is_done

    def get_status(self) -> str:
        return "Done" if self.is_done else "In progress"

    def __str__(self) -> str:
        return f"[{self.get_status()}] -> {self.title}"


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        task = Task(title)
        self.tasks.append(task)
        return task

    def remove_task(self, task_num: int) -> bool:
        index = task_num - 1
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_task(self, task_num: int) -> Task | None:
        index = task_num - 1
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def get_tasks(self) -> list[Task]:
        return self.tasks

    def toggle_task(self, task_num: int) -> bool:
        task = self.get_task(task_num)
        if task:
            task.toggle()
            return True
        return False

    def get_display_list(self) -> str:
        if not self.tasks:
            return "No tasks yet."
        lines = ["Tasks:"]
        for i, task in enumerate(self.tasks, start=1):
            lines.append(f"[{i}] {task}")
        return "\n".join(lines)


def main() -> None:
    task_manager = TaskManager()
    task_manager.add_task("Buy groceries")
    task_manager.add_task("Learn Python")
    task_manager.add_task("Sleep")

    task_manager.toggle_task(1)
    print(task_manager.get_display_list())

    task_manager.remove_task(2)
    task_manager.toggle_task(2)
    print(task_manager.get_display_list())

    task_manager.remove_task(2)
    print(task_manager.get_display_list())


if __name__ == "__main__":
    main()

# OUTPUT:
# Tasks:
# [1] [Done] -> Buy groceries
# [2] [In progress] -> Learn Python
# [3] [In progress] -> Sleep
# Tasks:
# [1] [Done] -> Buy groceries
# [2] [Done] -> Sleep
# Tasks:
# [1] [Done] -> Buy groceries
