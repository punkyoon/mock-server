from rest_framework import serializers
from rest_framework_serializer_extensions.fields import HashIdField

from todo_apps.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    id = HashIdField(model=ToDo, read_only=True)

    class Meta:
        model = ToDo
        fields = ('id', 'contents', 'isDone', )
