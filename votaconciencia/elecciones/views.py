from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from models import *

def index (request):
    return render_to_response('home/index.html',
    context_instance=RequestContext(request)
    )

def index_elecciones(request):
    return render(request, 'home/elecciones_index.html', {'elecciones': Eleccion.objects.all()})


def eleccion_individual(request, id):
    tuplas = []

    for partido in Partido.objects.all():
        p = partido
        candidatos = Candidato.objects.filter(eleccion__id=id)
        tuplas.append((p, candidatos))

    dictionary = {
        'partido_candidatos' : tuplas,
        'eleccion': Eleccion.objects.get(id=id)
    }

    return render(request, 'home/eleccion_individual.html', dictionary)
