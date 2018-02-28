from django.contrib import admin

# Register your models here.
from facturas.models import *

admin.site.register(Factura)
admin.site.register(Producto)
admin.site.register(Item)