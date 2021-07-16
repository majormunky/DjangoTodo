from rest_framework import serializers
from home import models


class TodoListSerializer(serializers.ModelSerializer):
    todo_count = serializers.SerializerMethodField()

    class Meta:
        model = models.TodoList
        fields = ["id", "name", "user", "todo_count", "created_at"]

    def get_todo_count(self, obj):
        return obj.todo_set.count()


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = ["id", "text", "completed"]
