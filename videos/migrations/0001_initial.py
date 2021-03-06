# Generated by Django 2.0.1 on 2018-01-12 05:31

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_smalluuid.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('editors', models.ManyToManyField(related_name='editable_channels', to=settings.AUTH_USER_MODEL)),
                ('moderators', models.ManyToManyField(related_name='moderated_channels', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', django_smalluuid.models.SmallUUIDField(default=django_smalluuid.models.UUIDDefault(), editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('views', models.PositiveIntegerField(default=0)),
                ('video', cloudinary.models.CloudinaryField(max_length=255, verbose_name='video')),
                ('description', models.CharField(max_length=1024)),
                ('view_fee', models.PositiveIntegerField(default=1)),
                ('rating', models.CharField(choices=[('General', 'G'), ('Parental Guidance', 'PG'), ('Parents Strongly Cautioned', 'PG-13'), ('Restricted', 'R'), ('Adults Only', 'NC-17')], default='PG-13', max_length=16)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Channel')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
