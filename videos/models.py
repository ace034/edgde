from django.db import models
from cloudinary.models import CloudinaryField

from core.models import UUIDModel

class Channel(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)

    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    editors = models.ManyToManyField('accounts.Account', related_name='editable_channels')
    moderators = models.ManyToManyField('accounts.Account', related_name='moderated_channels')


VIDEO_RATINGS = (
    ('General', 'G'),
    ('Parental Guidance', 'PG'),
    ('Parents Strongly Cautioned', 'PG-13'),
    ('Restricted', 'R'),
    ('Adults Only', 'NC-17'),
)

class Video(UUIDModel):
    title = models.CharField(max_length=128)
    views = models.PositiveIntegerField(default=0)
    video = CloudinaryField('video')
    description = models.CharField(max_length=1024)
    view_fee = models.PositiveIntegerField(default=1)
    rating = models.CharField(max_length=16, choices=VIDEO_RATINGS, default='PG-13')

    channel = models.ForeignKey('videos.Channel', on_delete=models.CASCADE)
    tags = models.ForeignKey('videos.Tag', on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=32)
