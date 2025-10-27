from django.test import TestCase
from django.urls import reverse
from todo.models import Task


class TaskListViewTest(TestCase):
    def test_task_list_view(self):
        # Ensures proper task list view.
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tasks")
