from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from home.api import serializers
from home import models


class TodoListDetailAPIView(views.APIView):
    def get(self, request, pk):
        try:
            data = models.TodoList.objects.get(pk=pk)
            todo_items = models.Todo.objects.filter(todo_list=data)
        except models.TodoList.DoesNotExist:
            return Response(
                "Unable to find TodoList",
                status=status.HTTP_400_BAD_REQUEST,
            )
        json_data = serializers.TodoSerializer(todo_items, many=True).data
        return Response(json_data)


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
        try:
            new_todo_list.save()
        except IntegrityError:
            return Response(
                "Unable to create Todo List, there is already one with that name",
                status=status.HTTP_400_BAD_REQUEST,
            )
        json_data = serializers.TodoListSerializer(new_todo_list).data
        return Response(json_data)
