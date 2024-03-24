# models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    description = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)