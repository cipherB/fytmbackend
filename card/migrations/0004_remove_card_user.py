# Generated by Django 4.0.3 on 2022-04-04 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_attachment__id_card__id_checklist__id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='user',
        ),
    ]
