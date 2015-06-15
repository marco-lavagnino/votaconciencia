from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from models import *
from elecciones.models import Eleccion

def calendario (request):
    return render(request, 'home/calendario.html', {})

def calendario_eventos (request):
    result = []
    start = request.GET['start']
    end = request.GET['end']
    for fecha in FechaImportante.objects.filter(fecha__range=[start, end]):
        result.append({
            'allDay': True,
            'title' : fecha.titulo,
            'start' : fecha.fecha
            })
    for eleccion in Eleccion.objects.filter(fecha__range=[start, end]):
        result.append({
            'allDay': True,
            'url'   : eleccion.get_absolute_url(),
            'title' : eleccion.nombre,
            'start' : eleccion.fecha
            })
    return JsonResponse(result, safe=0)
