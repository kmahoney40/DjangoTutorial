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
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
         
class RunTimesAudit(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    
class Temp(models.Model):
    t1 = models.DecimalField(max_digits=8, decimal_places=5)
    t2 = models.DecimalField(max_digits=8, decimal_places=5)
    t3 = models.DecimalField(max_digits=8, decimal_places=5)
    t4 = models.DecimalField(max_digits=8, decimal_places=5)
    t5 = models.DecimalField(max_digits=8, decimal_places=5)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
