from django.shortcuts import render

# Create your views here.

from facturas.models import *

def inicio(request):
    return render(request, 'index.html')