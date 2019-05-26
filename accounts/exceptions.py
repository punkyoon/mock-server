from rest_framework import status
from rest_framework.exceptions import APIException


class ProfileDoesNotExist(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'User profile does not exist'
    default_code = '400_PROFILE_DOES_NOT_EXIST'
