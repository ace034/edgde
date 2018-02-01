from django.db import models
from django_smalluuid.models import SmallUUIDField, uuid_default
from cloudinary.models import CloudinaryField

class UUIDModel(models.Model):
    id = SmallUUIDField(default=uuid_default(), primary_key=True, editable=False)

    class Meta:
        abstract = True


class PhotoModel(models.Model):
  image = CloudinaryField('image')

  class Meta:
      abstract = True
