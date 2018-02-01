from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

COLOR_CHOICES = (
    ('yellow', 'Yellow'),
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('pink', 'Pink'),
    ('gray', 'Gray'),
    ('black', 'Black'),
    ('orange', 'Orange'),
)

class Settings(models.Model):
    color = models.CharField(max_length=16, choices=COLOR_CHOICES, default='red')

    class Meta:
        verbose_name_plural = 'Settings'

class Account(AbstractUser):
    birthday = models.DateTimeField(null=True, blank=True)
    points = models.PositiveIntegerField(default=500)
    image = models.ImageField(upload_to='profile_image', blank=True)

    settings = models.OneToOneField('accounts.Settings', on_delete=models.CASCADE)

@receiver(pre_save, sender=Account)
def create_account_settings(sender, instance, *args, **kwargs):
    if not hasattr(instance, 'settings'):
        instance.settings = Settings.objects.create(account=instance)
