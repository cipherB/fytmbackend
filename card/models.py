from email.policy import default
from random import choices
from django.db import models
from board.models import Board
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Card(models.Model):
    STATUS_OPTION = (
        ('open', 'Open'),
        ('in progress', 'In Progress'),
        ('need assistance', 'Need Assistance'),
        ('on hold', 'On Hold'),
        ('client review', 'Client Review'),
        ('verify and close', 'Verify and Close'),
        ('done', 'done'),
    )
    PRIORITY_OPTION = (
        ('urgent', 'Urgent'),
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
        ('no priority', 'No Priority'),
    )
    board = models.ForeignKey(Board, default=None, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    assigned = models.ManyToManyField(User, blank=True, related_name="assigned_members")
    start_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=60, choices=STATUS_OPTION, default="open")
    priority = models.CharField(max_length=60, choices=PRIORITY_OPTION, default="no priority")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f" {self.name}"

class Attachment(models.Model):

    class FileAttachment(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='file')

    class ImageAttachment(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='image')

    class LinkAttachment(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(type='link')

    FILE_TYPE = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link')
    )
    card = models.ForeignKey(Card, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/", blank=True, null=True)
    file = models.FileField(upload_to="files/", blank=True, null=True)
    link_title = models.CharField(max_length=30, blank=True, null=True)
    link = models.CharField(max_length=160, blank=True, null=True)
    type = models.CharField(max_length=50, choices=FILE_TYPE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    imageObjects = ImageAttachment()
    fileObjects = FileAttachment()
    linkObjects = LinkAttachment()


    def __str__(self):
        return f" {self.type}"

class Comments(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.text}"

class CheckList(models.Model):
    card = models.ForeignKey(Card, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title}"
