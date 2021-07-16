from rest_framework import views
from rest_framework.response import Response
from home.api import serializers
from home import models


class TodoListAPIView(views.APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        todo_lists = models.TodoList.objects.filter(user=request.user)
        json_lists = serializers.TodoListSerializer(todo_lists, many=True).data
        return Response(json_lists)
