# Generated by Django 4.0.3 on 2022-04-07 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_remove_card_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='_id',
        ),
        migrations.RemoveField(
            model_name='card',
            name='_id',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='_id',
        ),
    ]
