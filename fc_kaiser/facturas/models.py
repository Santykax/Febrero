from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Factura(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1)
    tipob = models.BooleanField()
    

class Item(models.Model):
    producto = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()