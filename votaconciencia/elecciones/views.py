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


def index_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'home/index_candidatos.html',{"candidatos":candidatos})

def eleccion_individual(request, id):
    tuplas = []

    for partido in Partido.objects.all():
        p = partido
        candidatos = Candidato.objects.filter(eleccion__id=id)
        tuplas.append((p, candidatos))

def index_perfil(request, idc):
    candidato = get_object_or_404(Candidato, pk=idc)
    propuestas = Propuesta.objects.all().filter(candidato__id=idc)
    ctx = {"candidato":candidato,"propuestas":propuestas}
    return render(request, 'home/index_perfil.html',ctx)

    dictionary = {
        'partido_candidatos' : tuplas,
        'eleccion': Eleccion.objects.get(id=id)
    }

    return render(request, 'home/eleccion_individual.html', dictionary)
