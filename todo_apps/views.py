from rest_framework import viewsets, permissions
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin, ExternalIdViewMixin

from todo_apps.models import ToDo
from todo_apps.serializers import ToDoSerializer


class TodoView(ExternalIdViewMixin, SerializerExtensionsAPIViewMixin, viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(mock_user=self.request.user)
