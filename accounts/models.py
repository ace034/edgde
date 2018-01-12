from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

COLOR_CHOICES = (
    ('Yellow', 'yellow'),
    ('Red', 'red'),
    ('Blue', 'blue'),
    ('Green', 'green'),
    ('Gray', 'gray'),
    ('Black', 'black'),
    ('Orange', 'orange'),
)

class Settings(models.Model):
    color = models.CharField(max_length=16, choices=COLOR_CHOICES, default='red')

class Account(AbstractUser):
    birthday = models.DateTimeField()
    points = models.PositiveIntegerField(default=500)

    settings = models.OneToOneField('accounts.Settings', on_delete=models.CASCADE)

@receiver(pre_save, sender=Account)
def create_account_settings(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'settings'):
        instance.settings = Settings.objects.create(account=instance)
