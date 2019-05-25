from hashlib import blake2s
from time import time

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.db import models

from django_countries.fields import CountryField
from safedelete import DELETED_VISIBLE_BY_PK
from safedelete.managers import SafeDeleteManager

from mock_server.models import BaseModel


class AbstractMockUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator],)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)    # Send an email to this user


class MockUserManager(UserManager, SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK


class MockUser(BaseModel, AbstractMockUser):
    objects = MockUserManager()

    class Meta:
        ordering = ['-id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create(cls, email, password, language, country, locale):
        username = cls.generate_username()

        mock_user = cls.objects.create(email=email, username=username)
        mock_user.set_password(password)
        mock_user.save()

        MockProfile.create(mock_user=mock_user, language=language, country=country, locale=locale)

        return mock_user

    @classmethod
    def generate_username(cls):
        current_timestamp = f'{int(time())}'
        blake_hash = blake2s(digest_size=4, key=b'mock-server-key')    # 8-length
        blake_hash.update(current_timestamp.encode('utf-8'))

        return blake_hash.hexdigest()


class MockProfile(BaseModel):
    mock_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(default='', max_length=65)

    language = models.CharField(blank=True, default='', max_length=2)    # ko, ja, en, ...
    country = CountryField(blank=True, default='')  # NZ, KR, ...
    locale = models.CharField(blank=True, default='', max_length=5)   # ko-KR, en-US, ...

    class Meta:
        ordering = ['-id']

    @classmethod
    def create(cls, mock_user, language='', country='', locale=''):
        mock_profile = MockProfile.objects.create(
            mock_user=mock_user, language=language, country=country, locale=locale
        )
        return mock_profile
