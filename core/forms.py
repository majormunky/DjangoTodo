from django.contrib.auth.forms import UserCreationForm
from .models import CoreUser


class CoreUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CoreUser
        fields = ["email", "first_name", "last_name"]
