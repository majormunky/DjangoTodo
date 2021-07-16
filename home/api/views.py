from rest_framework import views
from rest_framework import generics
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


class TodoListCreateAPIView(generics.CreateAPIView):
    def post(self, request):
        print(request.POST)
        name = request.POST.get("name")
        new_todo_list = models.TodoList(name=name, user=request.user)
        new_todo_list.save()
        json_data = serializers.TodoListSerializer(new_todo_list).data
        return Response(json_data)
