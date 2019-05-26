from django.urls import path

from rest_auth.views import LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from accounts.views import RegisterMockUserView, FetchMockProfileView


app_name = 'accounts'
urlpatterns = [
    path(r'login', obtain_jwt_token, name='login'),
    path(r'logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterMockUserView.as_view(), name='register'),
    path(r'profile', FetchMockProfileView.as_view(), name='profile'),

    path(r'password/change', PasswordChangeView.as_view(), name='password_change'),
    path(r'password/reset', PasswordResetView.as_view(), name='password_reset'),
    path(r'password/reset/confirm', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('token/refresh', refresh_jwt_token),
    path('token/verify', verify_jwt_token),
]

# More details: https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html#basic
