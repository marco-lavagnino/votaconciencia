from django.shortcuts import render, get_object_or_404
from models import *
from elecciones.models import Eleccion
from django.db.models import Q


def index_entrevistas (request):
    # elecciones = Eleccion.objects.filter(postulaciones__candidato__entrevist__count__gt=0).order_by('-fecha')
    tienen_candidatos = EntrevistaCandidato.objects.values('entrevistado__postulaciones__cargo__eleccion__id').distinct()
    tienen_personalidades = EntrevistaPersonalidad.objects.values('eleccion__id').distinct()
    elecciones = Eleccion.objects.filter(Q(id__in=tienen_candidatos) | Q(id__in=tienen_personalidades))
    return render(request, "entrevistas/index.html", {'elecciones' : elecciones})

def entrevista_individual (request, id):
    try:
        entrevista = EntrevistaCandidato.objects.get(id=id)
    except EntrevistaCandidato.DoesNotExist:
        try:
            entrevista = EntrevistaPersonalidad.objects.get(id=id)
        except EntrevistaPersonalidad.DoesNotExist:
            entrevista = get_object_or_404(Entrevista, id=id)
    return render(request, "entrevistas/individual.html", {'entrevista':entrevista})
