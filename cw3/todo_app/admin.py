from django.contrib import admin

from .models import Todo, TodoList

# Register your models here.


admin.site.register(TodoList)
admin.site.register(Todo)