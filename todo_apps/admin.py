from django.contrib import admin

from todo_apps.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('mock_user', 'created', 'modified', 'contents', 'isDone')
    fields = ('contents', 'isDone', )
