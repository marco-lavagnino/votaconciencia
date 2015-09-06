from django.shortcuts import render, get_object_or_404
from models import *
from elecciones.models import Eleccion


def index_entrevistas (request):
    elecciones = Eleccion.objects.order_by('-fecha')
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
