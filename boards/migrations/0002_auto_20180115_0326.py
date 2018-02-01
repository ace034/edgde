# Generated by Django 2.0.1 on 2018-01-15 03:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='editable_boards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='boards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='moderated_boards', to=settings.AUTH_USER_MODEL),
        ),
    ]
