from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.exceptions import ProfileDoesNotExist
from accounts.models import MockUser, MockProfile
from accounts.serializers import MockUserSerializer, MockProfileSerializer


class RegisterMockUserView(CreateAPIView):
    model = MockUser
    permission_classes = (AllowAny, )
    serializer_class = MockUserSerializer


class FetchMockProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = MockProfileSerializer

    def get_object(self):
        try:
            mock_profile = MockProfile.objects.get(mock_user=self.request.user)
        except MockProfile.DoesNotExist:
            raise ProfileDoesNotExist()
        else:
            return mock_profile
