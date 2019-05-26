from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-api/', include('rest_framework.urls')),

    path('accounts/', include('accounts.urls')),
    path('todo-apps/', include('todo_apps.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
