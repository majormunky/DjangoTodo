from rest_framework import serializers
from home import models


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoList
        fields = ["name", "user", "created_at"]
