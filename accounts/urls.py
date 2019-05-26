from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from accounts.views import MockUserView, MockProfileView


app_name = 'accounts'

mock_user = MockUserView.as_view({'post': 'create', 'get': 'retrieve'})
mock_profile = MockProfileView.as_view({'get': 'retrieve', 'put': 'update'})

urlpatterns = format_suffix_patterns([
    path('', mock_user, name='mock_user'),
    path('profile', mock_profile, name='mock_profile'),

    path('login', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
])
