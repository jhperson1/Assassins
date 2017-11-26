# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=200)
    alive = models.BooleanField()
    number_of_kills = models.IntegerField()
    time_killed = models.DateTimeField('time killed')
    assassin = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def is_alive(self):
        return self.alive

class KillFeed(models.Model):
    assassin = models.CharField(max_length=200)
    target = models.CharField(max_length=200)
    time = models.DateTimeField('time')
    epic_story = models.CharField(max_length=500)
    def __str__(self):
        return self.number