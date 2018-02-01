# Generated by Django 2.0.1 on 2018-01-15 03:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20180115_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='editable_channels', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='channel',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='moderated_channels', to=settings.AUTH_USER_MODEL),
        ),
    ]
