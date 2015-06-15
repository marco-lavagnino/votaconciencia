from django.shortcuts import render, get_object_or_404
from models import *

def index (request):
    return render(request, 'home/index.html', {})

def quienes_somos (request):
    descripcion = QuienesSomos.objects.last()
    return render(request, 'home/quienes_somos.html', {'descripcion': descripcion})
