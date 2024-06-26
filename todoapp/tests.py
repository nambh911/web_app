from django.test import TestCase
from .models import TodoItem

class TodoItemModelTest(TestCase):

    def setUp(self):
        TodoItem.objects.create(title="Test Todo", description="Test Description")

    def test_todo_creation(self):
        todo = TodoItem.objects.get(title="Test Todo")
        self.assertEqual(todo.description, "Test Description")

class TodoItemViewTest(TestCase):

    def setUp(self):
        self.todo = TodoItem.objects.create(title="Test Todo", description="Test Description")

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_add_todo_view(self):
        response = self.client.post('/add/', {'title': 'New Todo', 'description': 'New Description', 'completed': False})
        self.assertEqual(response.status_code, 302)  # Should redirect after adding
        self.assertEqual(TodoItem.objects.count(), 2)

    def test_update_todo_view(self):
        response = self.client.post(f'/update/{self.todo.pk}/', {'title': 'Updated Todo', 'description': 'Updated Description', 'completed': True})
        self.assertEqual(response.status_code, 302)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')
        self.assertTrue(self.todo.completed)

    def test_delete_todo_view(self):
        response = self.client.post(f'/delete/{self.todo.pk}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TodoItem.objects.count(), 0)
