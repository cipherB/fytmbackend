# Generated by Django 4.0.3 on 2022-04-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_useraccount_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='_id',
            field=models.CharField(blank=True, editable=False, max_length=16, unique=True),
        ),
    ]