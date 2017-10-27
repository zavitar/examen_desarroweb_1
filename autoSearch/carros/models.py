# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.conf import settings

# Create your models here.
class Car(models.Model):

    Marca = models.CharField(max_length = 150)
    Type = models.TextField()
    Year = models.CharField(max_length = 150)
    Colour = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.Marca)