from django.test import TestCase
from todo.models import Task

class TaskModelTest(TestCase):
    def test_create_task(self):
        # Proper Task Init. Testing
        task = Task.objects.create(title="Test Task")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.is_completed)
