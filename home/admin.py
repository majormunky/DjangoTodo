from django.contrib import admin
from home import models


admin.site.register(models.Todo)
admin.site.register(models.TodoList)
