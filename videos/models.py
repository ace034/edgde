from django.db import models

from core.models import UUIDModel

class Channel(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    editors = models.ManyToManyField('accounts.Account', related_name='editable_channels', blank=True)
    moderators = models.ManyToManyField('accounts.Account', related_name='moderated_channels', blank=True)


VIDEO_RATINGS = (
    ('G', 'General'),
    ('PG', 'Parental Guidance'),
    ('PG-13', 'Parents Strongly Cautioned'),
    ('R', 'Restricted'),
    ('NC-17', 'Adults Only'),
)

class Video(UUIDModel):
    title = models.CharField(max_length=128)
    views = models.PositiveIntegerField(default=0)
    video = models.FileField(upload_to='videos')
    description = models.CharField(max_length=1024)
    view_fee = models.PositiveIntegerField(default=1)
    rating = models.CharField(max_length=16, choices=VIDEO_RATINGS, default='PG-13')

    channel = models.ForeignKey('videos.Channel', on_delete=models.CASCADE)
    tags = models.ForeignKey('videos.Tag', on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=32)
