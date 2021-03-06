# Generated by Django 4.0.3 on 2022-04-02 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.CharField(blank=True, editable=False, max_length=16, primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('link_title', models.CharField(blank=True, max_length=30, null=True)),
                ('link', models.CharField(blank=True, max_length=160, null=True)),
                ('type', models.CharField(choices=[('image', 'Image'), ('file', 'File'), ('link', 'Link')], max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.CharField(blank=True, editable=False, max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('in progress', 'In Progress'), ('need assistance', 'Need Assistance'), ('on hold', 'On Hold'), ('client review', 'Client Review'), ('verify and close', 'Verify and Close'), ('done', 'done')], default='open', max_length=60)),
                ('priority', models.CharField(choices=[('urgent', 'Urgent'), ('high', 'High'), ('normal', 'Normal'), ('low', 'Low'), ('no priority', 'No Priority')], default='no priority', max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.CharField(blank=True, editable=False, max_length=16, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('card', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='card.card')),
            ],
        ),
    ]
