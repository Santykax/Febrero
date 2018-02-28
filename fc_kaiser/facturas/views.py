from django.shortcuts import render

# Create your views here.

from facturas.models import *

def inicio(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    items = Item.objects.all()
    montoT = items.precio * items.cantidad
    return render(request, 'index.html', {'factura':factura, 'items':factura.items.all()})


def iva(montoT):
    facturas = Factura.objects.all()
    if (facturas.tipo == true):
        montoT * 1.21
    return render(montoT)