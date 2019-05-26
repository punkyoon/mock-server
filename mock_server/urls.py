from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-api/', include('rest_framework.urls')),

    path('accounts/', include('accounts.urls')),
]
