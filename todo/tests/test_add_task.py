from django.test import TestCase
from django.urls import reverse
from todo.models import Task


class TaskAddViewTest(TestCase):
    def test_add_task_view_creates_new_task(self):
        # Sends to create a new task and then return to task list.
        response = self.client.post(reverse("task_add"), {"title": "New Task"})
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "New Task")
        self.assertEqual(response.status_code, 302)
