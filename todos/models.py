from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/todos/{self.id}'
