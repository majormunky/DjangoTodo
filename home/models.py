from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model


class TodoList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(default=timezone.now)


class Todo(models.Model):
    text = models.CharField(max_length=512)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
