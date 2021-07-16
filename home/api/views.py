from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from home.api import serializers
from home import models


class TodoListDetailAPIView(views.APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        todo_lists = models.TodoList.objects.filter(user=request.user)
        json_lists = serializers.TodoListSerializer(todo_lists, many=True).data
        return Response(json_lists)


class TodoListCreateAPIView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
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


class TodoCreateAPIView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.POST.get("text")
        todo_list_id = request.POST.get("todo_list_id")
        try:
            todo_list = models.TodoList.objects.get(pk=todo_list_id)
        except models.TodoList.DoesNotExist:
            return Response(
                "Unable to find todo list", status=status.HTTP_400_BAD_REQUEST
            )

        new_todo = models.Todo(todo_list=todo_list, text=text)
        new_todo.save()

        json_data = serializers.TodoSerializer(new_todo).data
        return Response(json_data)
