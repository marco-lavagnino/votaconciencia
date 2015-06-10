from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from models import *

def index (request):
    return render(request, 'home/index.html', {})


# VIEWS DE ELECCIONES
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



# VIEWS DE CANDIDATOS
def index_candidatos(request):
    elecciones = Eleccion.objects.all()
    return render(request, 'candidato/index.html', {"elecciones": elecciones})

def perfil_candidato(request, idc):
    candidato = get_object_or_404(Candidato, pk=idc)
    return render(request, 'candidato/perfil.html', {"candidato":candidato})



# VIEWS DE PARTIDOS
def index_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partido/index.html',{"partidos":partidos})

def perfil_partido(request,idp):
    partido = get_object_or_404(Partido, pk=idp)
    return render(request, 'partido/perfil.html', {"partido":partido})



def calendario (request):
    return render(request, 'home/calendario.html', {})