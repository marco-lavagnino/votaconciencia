# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import *
from partidos.models import Partido
from candidatos.models import Candidato


def index_elecciones(request):
    return render(request, 'eleccion/index.html', {'elecciones': Eleccion.objects.all()})

def perfil_eleccion(request, id):
    tuplas = []
    for partido in Partido.objects.all():
        p = partido
        candidatos = Candidato.objects.filter(eleccion__id=id,partido__id=partido.id)
        if candidatos:
            tuplas.append((p, candidatos))
    dictionary = {
        'partido_candidatos' : tuplas,
        'eleccion': Eleccion.objects.get(id=id)
    }
    return render(request, 'eleccion/perfil.html', dictionary)
