from rest_framework import serializers
from rest_framework_serializer_extensions.fields import HashIdField
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

from accounts.models import MockUser, MockProfile


class MockUserSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=MockUser, read_only=True)

    password = serializers.CharField(write_only=True, max_length=128)

    nickname = serializers.CharField(write_only=True, max_length=65)
    locale = serializers.CharField(write_only=True, max_length=5)

    class Meta:
        model = MockUser
        fields = ('id', 'email', 'password', 'nickname', 'locale', )

    def create(self, validated_data):
        # validated_data: email, password, locale
        return MockUser.create(**validated_data)


class MockProfileSerializer(SerializerExtensionsMixin, serializers.ModelSerializer):
    id = HashIdField(model=MockProfile, read_only=True)

    class Meta:
        model = MockProfile
        fields = ('id', 'nickname', 'created', 'locale', 'profile_image')
        read_only_fields = ('created', 'locale', )
