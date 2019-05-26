from django.db import models

from accounts.models import MockUser
from mock_server.models import BaseModel


class ToDo(BaseModel):
    mock_user = models.ForeignKey(MockUser, on_delete=models.CASCADE)
    contents = models.TextField()
    isDone = models.BooleanField(default=False)
