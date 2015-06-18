# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import *
from partidos.models import Partido
from candidatos.models import Candidato

def agrupa_por_representacion(**kwargs):
    grupos_candidatos = {}
    for candidato in Candidato.objects.filter(**kwargs):
        try:
            grupos_candidatos[candidato.representa_a()] += [candidato]
        except KeyError:
            grupos_candidatos[candidato.representa_a()] = [candidato]
    return grupos_candidatos.items()

def index_elecciones(request):
    return render(request, 'eleccion/index.html', {'elecciones': Eleccion.objects.all()})

def eleccion_intermedio(request, id):
    eleccion = get_object_or_404(Eleccion, pk=id)
    return render(request, 'eleccion/intermedio.html', {'eleccion':eleccion})

def eleccion_informacion(request, id):
    eleccion = get_object_or_404(Eleccion, pk=id)
    return render(request, 'eleccion/informacion.html', {'eleccion':eleccion})

def eleccion_candidatos(request, id):
    dictionary = {
        'candidatos' : agrupa_por_representacion(eleccion__id=id, legislador=False),
        'legisladores' : agrupa_por_representacion(eleccion__id=id, legislador=True),
        'eleccion': Eleccion.objects.get(id=id)
    }
    return render(request, 'eleccion/candidatos.html', dictionary)
