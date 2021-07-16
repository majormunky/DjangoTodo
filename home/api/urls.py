from django.urls import path
from home.api import views

urlpatterns = [
    path("todo-list/", views.TodoListAPIView.as_view()),
    path("todo-list/create/", views.TodoListCreateAPIView.as_view()),
    path("todo-list/<int:pk>/", views.TodoListDetailAPIView.as_view()),
    path("todo/create/", views.TodoCreateAPIView.as_view()),
    path("todo/update/", views.TodoUpdateAPIView.as_view()),
]
