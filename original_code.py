class TaskManager:
    def __init__(self):
        self.tasks = []
        self.tasks.append({"title": "Купити хліб", "description": "Продуктовий магазин", "priority": "середній", "done": False})
        self.tasks.append({"title": "Підготуватись до іспиту", "description": "Прочитати конспект", "priority": "високий", "done": False})

    def add_task(self, title, description, priority):
        self.tasks.append({"title": title, "description": description, "priority": priority, "done": False})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            status = "Зроблено" if task["done"] else "Не зроблено"
            return f"{task['title']} - {task['priority']} - {status}\n{task['description']}"
        return "Невірний індекс"

    def list_pending_tasks(self):
        return "\n".join(f"{i+1}. {t['title']} - {t['priority']}"
                         for i, t in enumerate(self.tasks) if not t["done"])

    def list_completed_tasks(self):
        return "\n".join(f"{i+1}. {t['title']} - {t['priority']}"
                         for i, t in enumerate(self.tasks) if t["done"])

    def __str__(self):
        return "\n".join([f"{i+1}. {t['title']} - {t['priority']} - {'Зроблено' if t['done'] else 'Не зроблено'}"
                          for i, t in enumerate(self.tasks)])
