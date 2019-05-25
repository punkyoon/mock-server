from django.contrib.auth.backends import ModelBackend

from accounts.models import MockUser


class EmailAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = MockUser.objects.get(email=username)
        except MockUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

        return None
