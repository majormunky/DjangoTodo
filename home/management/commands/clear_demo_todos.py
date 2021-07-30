from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from home import models


class Command(BaseCommand):
    help = "Clears out any todos created by the demo account"

    def handle(self, *args, **options):
        demo_account = get_user_model().objects.filter(email="demo@example.com")
        if demo_account:
            todo_list = models.Todo.objects.filter(user=demo_account.first())
            todo_list.delete()
