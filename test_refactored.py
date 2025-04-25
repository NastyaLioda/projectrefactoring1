import unittest
from refactored_code import TaskManager, Task

class TestRefactoredTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Погуляти", "Прогулянка парком", "низький")
        self.assertEqual(len(self.manager.tasks), 3)

    def test_delete_task(self):
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.tasks), 1)

    def test_invalid_index_delete(self):
        self.manager.delete_task(10)
        self.assertEqual(len(self.manager.tasks), 2)

    def test_mark_done(self):
        self.manager.mark_task_done(0)
        self.assertTrue(self.manager.tasks[0].done)

    def test_invalid_index_mark_done(self):
        self.manager.mark_task_done(5)
        self.assertFalse(any(task.done for task in self.manager.tasks))

    def test_initial_done_status(self):
        self.assertFalse(self.manager.tasks[1].done)

    def test_done_status_after_marking(self):
        self.manager.mark_task_done(0)
        self.assertTrue(self.manager.tasks[0].done)

    def test_add_and_delete(self):
        self.manager.add_task("Test", "Desc", "низький")
        self.manager.delete_task(2)
        self.assertEqual(len(self.manager.tasks), 2)

    def test_delete_all_tasks(self):
        self.manager.delete_task(0)
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_mark_multiple_done(self):
        self.manager.mark_task_done(0)
        self.manager.mark_task_done(1)
        self.assertTrue(all(t.done for t in self.manager.tasks))

    def test_task_properties(self):
        task = self.manager.tasks[0]
        self.assertEqual(task.title, "Купити хліб")
        self.assertEqual(task.priority, "середній")

    def test_empty_task_list_delete(self):
        self.manager.delete_task(0)
        self.manager.delete_task(0)
        self.manager.delete_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_empty_task_list_mark_done(self):
        self.manager.delete_task(0)
        self.manager.delete_task(0)
        self.manager.mark_task_done(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_str_output_contains(self):
        output = str(self.manager)
        self.assertIn("Купити хліб", output)

    def test_str_output_format(self):
        output = str(self.manager)
        self.assertIn("1. Купити хліб - середній - Не зроблено", output)

    def test_add_task_content(self):
        self.manager.add_task("Новий", "Опис", "високий")
        task = self.manager.tasks[-1]
        self.assertEqual(task.description, "Опис")

    def test_priority_check(self):
        self.assertEqual(self.manager.tasks[1].priority, "високий")

    def test_task_list_type(self):
        self.assertIsInstance(self.manager.tasks, list)

    def test_task_instance(self):
        self.assertIsInstance(self.manager.tasks[0], Task)
