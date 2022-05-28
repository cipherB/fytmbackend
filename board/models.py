from django.db import models
from workspace.models import Workspace
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=160)
    # user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, default=None, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, blank=True, related_name="members")
    color_theme_1 = models.CharField(max_length=20, blank=True, null=True)
    color_theme_2 = models.CharField(max_length=20, blank=True, null=True)
    color_theme_3 = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     self._id = get_random_string(length=16)
    #     super(Board, self).save(*args, **kwargs)

    def __str__(self):
        return f" {self.name}"

