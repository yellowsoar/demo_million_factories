import uuid

from django.db import models
from django.contrib.gis.db import models as gmodels

# Create your models here.


class Factory(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID",
    )
    location = gmodels.PointField(
        blank=True,
        null=True,
        srid=4326,
    )
