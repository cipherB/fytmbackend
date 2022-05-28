from django.db import models
# from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ActivityLog(models.Model):
    class WorkspaceActivity(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='workspace')

    class BoardActivity(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='board')

    class CardActivity(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='card')

    ACTIVITY_TYPE = (
        ('workspace', 'Workspace'),
        ('board', 'Board'),
        ('card', 'Card')
    )

    # id = models.CharField(max_length=16, primary_key=True, editable=False, blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    type= models.CharField(max_length=20, choices=ACTIVITY_TYPE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    workspaceObjects = WorkspaceActivity()
    boardObjects = BoardActivity()
    cardObjects = CardActivity()



    # def save(self, *args, **kwargs):
    #     self.id = get_random_string(length=16)
    #     super(ActivityLog, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}, {self.description}"

    class Meta:
        ordering= ("-created_at",)
