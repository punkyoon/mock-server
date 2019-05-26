from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from todo_apps.views import TodoView

app_name = 'todo_apps'

todo_list = TodoView.as_view({'post': 'create', 'get': 'list'})
todo_detail = TodoView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})

urlpatterns = format_suffix_patterns([
    path('', todo_list, name='todo_list'),
    path('<str:pk>/', todo_detail, name='todo_detail'),
])
