from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='first todo', body='first todo body')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'first todo body')

    def test_object_name_is_title(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = todo.title
        self.assertEquals(expected_object_name, str(todo))

    def test_get_absolute_url(self):
        todo = Todo.objects.get(id=1)
        self.assertEquals(todo.get_absolute_url(), '/todos/1')


class TodoAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='first todo', body='first todo body')

    def test_get_list(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        response = self.client.get(reverse('todo_detail', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        response = self.client.post(reverse('todo_list'), {'title': 'new todo', 'body': 'new todo body'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        response = self.client.put(reverse('todo_detail', kwargs={'pk': self.todo.pk}),
                                   {'title': 'updated todo', 'body': 'updated todo body'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(reverse('todo_detail', kwargs={'pk': self.todo.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
