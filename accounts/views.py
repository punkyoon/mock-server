from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin, ExternalIdViewMixin

from accounts.exceptions import ProfileDoesNotExist
from accounts.models import MockProfile
from accounts.serializers import MockUserSerializer, MockProfileSerializer


class MockUserView(ExternalIdViewMixin, SerializerExtensionsAPIViewMixin,
                   mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = MockUserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return (permission() for permission in (AllowAny, ))
        return super().get_permissions()    # (IsAuthenticated, )

    def get_object(self):
        return self.request.user


class MockProfileView(ExternalIdViewMixin, SerializerExtensionsAPIViewMixin,
                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = MockProfileSerializer

    def get_object(self):
        try:
            mock_profile = MockProfile.objects.get(mock_user=self.request.user)
        except MockProfile.DoesNotExist:
            raise ProfileDoesNotExist()
        else:
            return mock_profile
