from django.test import TestCase
from todo.models import Task, SubTask


class SubTaskModelTest(TestCase):
    def test_create_subtask(self):
        # Checks that subtasks are properly linked.
        parent = Task.objects.create(title="Main Task")
        sub = SubTask.objects.create(title="Part A", parent=parent)
        self.assertEqual(sub.parent, parent)
        self.assertFalse(sub.is_completed)
        self.assertEqual(str(sub), "Part A → Main Task")
