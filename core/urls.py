from django.urls import path
from . import views

urlpatterns = [
    path("register-user/", views.register_user, name="register-user"),
    path(
        "registration-complete/",
        views.registration_complete,
        name="registration-complete",
    ),
]
