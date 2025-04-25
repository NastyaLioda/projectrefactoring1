from dataclasses import dataclass

@dataclass
class Task:
    title: str
    description: str
    priority: str
    done: bool = False

    def mark_done(self):
        self.done = True

    def is_done(self) -> bool:
        return self.done

    def __str__(self):
        status = "Зроблено" if self.done else "Не зроблено"
        return f"{self.title} - {self.priority} - {status}\n{self.description}"


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = [
            Task("Купити хліб", "Продуктовий магазин", "середній"),
            Task("Підготуватись до іспиту", "Прочитати конспект", "високий")
        ]

    def add_task(self, title: str, description: str, priority: str):
        self.tasks.append(Task(title, description, priority))

    def delete_task(self, index: int) -> str:
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            return f"Задачу '{removed.title}' видалено."
        return "Невірний індекс"

    def mark_task_done(self, index: int) -> str:
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            return f"Задача '{self.tasks[index].title}' позначена як виконана."
        return "Невірний індекс"

    def get_task(self, index: int) -> str:
        if 0 <= index < len(self.tasks):
            return str(self.tasks[index])
        return "Невірний індекс"

    def list_pending_tasks(self) -> str:
        return "\n".join(f"{i+1}. {task.title} - {task.priority}"
                         for i, task in enumerate(self.tasks) if not task.is_done())

    def list_completed_tasks(self) -> str:
        return "\n".join(f"{i+1}. {task.title} - {task.priority}"
                         for i, task in enumerate(self.tasks) if task.is_done())

    def __str__(self) -> str:
        return "\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))
