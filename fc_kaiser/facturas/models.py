from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Factura(models.Model):
    cliente = models.CharField(max_length=50)
    tipo_A = models.BooleanField()
    
    def __str__(self):
        return '{}/Tipo: {}'.format(self.cliente, self.tipo_A)
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre)
 

class Item(models.Model):
    facturas = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="items")
    productos = models.OneToOneField(Producto)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return 'Cliente: {}/Producto: {}/Precio: ${}/Cantidad: {}'.format(self.facturas.cliente, self.productos.nombre, self.precio, self.cantidad)
    
    