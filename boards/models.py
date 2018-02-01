import datetime
from django.db import models
from cloudinary.models import CloudinaryField

from core.models import UUIDModel

BOARD_RATINGS = (
    ('SFW', 'Safe For Work'),
    ('NSFW', 'Not Safe For Work'),
)

class Board(UUIDModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    rating = models.CharField(max_length=4, choices=BOARD_RATINGS)
    image = models.ImageField('image', null=True, blank=True)

    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    editors = models.ManyToManyField('accounts.Account', related_name='editable_boards', blank=True)
    moderators = models.ManyToManyField('accounts.Account', related_name='moderated_boards', blank=True)
    members = models.ManyToManyField('accounts.Account', related_name='boards', blank=True)

class Membership(models.Model):
    fee = models.PositiveIntegerField(default=1)
    occurance = models.DurationField(default=datetime.timedelta(days=30))

class Post(UUIDModel):
    title = models.CharField(max_length=128)
    body = models.TextField()

    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE, related_name='posts')

    replies = models.ManyToManyField('boards.Post')
