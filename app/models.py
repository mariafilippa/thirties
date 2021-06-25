# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


class UserMapping(models.Model):
    user_hash = models.CharField(max_length=255)
    begin_time = models.DateTimeField()
    latitube = models.FloatField()
    month = models.IntegerField()
    location = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
