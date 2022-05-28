from django.contrib import admin
from .models import Card, CheckList, Attachment, Comments

# Register your models here.
admin.site.register(Card)
admin.site.register(CheckList)
admin.site.register(Attachment)
admin.site.register(Comments)
