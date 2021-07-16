from django.urls import path
from home.api import views

urlpatterns = [
    path("todo-list/", views.TodoListAPIView.as_view()),
]
