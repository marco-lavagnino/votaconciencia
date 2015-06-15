from django.shortcuts import render, get_object_or_404
from models import *

def index (request):
    return render(request, 'home/index.html', {})

def quienes_somos (request):
    contenido = QuienesSomos.objects.last().contenido
    return render(request, 'home/quienes_somos.html', {'contenido': contenido})
