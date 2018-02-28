from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Factura(models.Model):
    cliente = models.CharField(max_length=50)
    tipo_A = models.BooleanField()
    
    def __str__(self):
        return '/{}/Tipo: {}/'.format(self.cliente, self.tipo_A)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return '/{}/${}/Cantidad: {}'.format(self.nombre, self.precio, self.cantidad)
 

class Item(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.OneToOneField(Producto)
    
    def __str__(self):
        return '/Cliente: {}/Producto: {}/Precio: ${}/Cantidad: {}/'.format(self.factura.cliente, self.producto.nombre, self.producto.precio, self.producto.cantidad)
    
    