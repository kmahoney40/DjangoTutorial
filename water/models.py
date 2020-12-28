import datetime

from django.db import models
from django.utils import timezone

class RunTimes(models.Model):
    day = models.PositiveIntegerField(default=0)
    v1 = models.PositiveIntegerField(default=0)
    v2 = models.PositiveIntegerField(default=0)
    v3 = models.PositiveIntegerField(default=0)
    v4 = models.PositiveIntegerField(default=0)
    v5 = models.PositiveIntegerField(default=0)
    v6 = models.PositiveIntegerField(default=0)
    v7 = models.PositiveIntegerField(default=0)
    pub_date = models.DateTimeField('date published')
        