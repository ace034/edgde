import datetime

from django.db import models

from core.models import UUIDModel

BOARD_RATINGS = (
    ('Safe For Work', 'SFW'),
    ('Not Safe For Work', 'NSFW'),
)

class Board(UUIDModel):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    rating = models.CharField(max_length=4, choices=BOARD_RATINGS)

    owner = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    editors = models.ManyToManyField('accounts.Account', related_name='editable_boards')
    moderators = models.ManyToManyField('accounts.Account', related_name='moderated_boards')
    members = models.ManyToManyField('accounts.Account', related_name='boards')

class Membership(models.Model):
    fee = models.PositiveIntegerField(default=1)
    occurance = models.DurationField(default=datetime.timedelta(days=30))

class Post(UUIDModel):
    title = models.CharField(max_length=128)
    body = models.TextField()

    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE)

    replies = models.ManyToManyField('boards.Post')
