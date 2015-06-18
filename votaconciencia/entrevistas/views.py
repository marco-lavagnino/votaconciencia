from django.shortcuts import render, get_object_or_404
from models import *

# Create your views here.

def index_entrevistas (request):
    entrevistas = list(EntrevistaCandidato.objects.all())
    entrevistas += list(EntrevistaPersonalidad.objects.all())
    return render(request, "entrevistas/index.html", {'entrevistas' : entrevistas})

def entrevista_individual (request, id):
    try:
        entrevista = EntrevistaCandidato.objects.get(id=id)
    except EntrevistaCandidato.DoesNotExist:
        try:
            entrevista = EntrevistaPersonalidad.objects.get(id=id)
        except EntrevistaPersonalidad.DoesNotExist:
            entrevista = get_object_or_404(Entrevista, id=id)
    return render(request, "entrevistas/individual.html", {'entrevista':entrevista})
