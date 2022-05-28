from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=160)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name}"
