from dataclasses import dataclass

@dataclass
class Task:
    title: str
    description: str
    priority: str
    done: bool = False

    def __str__(self):
        status = "Зроблено" if self.done else "Не зроблено"
        return f"{self.title} - {self.priority} - {status}"


class TaskManager:
    def __init__(self):
        self.tasks: list[Task] = [
            Task("Купити хліб", "Продуктовий магазин", "середній"),
            Task("Підготуватись до іспиту", "Прочитати конспект", "високий")
        ]

    def add_task(self, title, description, priority):
        self.tasks.append(Task(title, description, priority))

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True

    def __str__(self):
        return "\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))
