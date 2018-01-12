from django.db import models
from django_smalluuid.models import SmallUUIDField, uuid_default

class UUIDModel(models.Model):
    id = SmallUUIDField(default=uuid_default(), primary_key=True, editable=False)
    
    class Meta:
        abstract = True
