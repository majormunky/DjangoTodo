from django.urls import path
from home.api import views

urlpatterns = [
    path("", views.TodoListAPIView.as_view()),
]
