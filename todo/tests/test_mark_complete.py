from django.test import TestCase
from django.urls import reverse
from todo.models import Task


class TaskCompleteViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Finish homework")

    def test_mark_complete_view(self):
        # Ensures task cam be marked complete via request.
        response = self.client.post(reverse("task_complete", args=[self.task.id]))
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_completed)
        self.assertEqual(response.status_code, 302)  # redirects to task list
