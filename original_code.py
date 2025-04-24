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

    def __str__(self):
        return "\n".join([f"{i+1}. {task['title']} - {task['priority']} - {'Зроблено' if task['done'] else 'Не зроблено'}"
                          for i, task in enumerate(self.tasks)])
