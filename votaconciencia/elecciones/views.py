# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import *
from partidos.models import Partido
from candidatos.models import Candidato
from django.db.models import F, Sum

def index_elecciones(request):
    return render(request, 'eleccion/index.html', {'elecciones': Eleccion.objects.all()})

def eleccion_intermedio(request, id):
    eleccion = get_object_or_404(Eleccion, pk=id)
    return render(request, 'eleccion/intermedio.html', {'eleccion':eleccion})

def eleccion_informacion(request, id):
    eleccion = get_object_or_404(Eleccion, pk=id)
    return render(request, 'eleccion/informacion.html', {'eleccion':eleccion})

def eleccion_candidatos(request, id):
    eleccion = get_object_or_404(Eleccion, pk=id)
    return render(request, 'eleccion/candidatos.html', {'eleccion':eleccion})
