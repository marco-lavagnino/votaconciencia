from django.shortcuts import render, get_object_or_404
from models import *
from elecciones.models import Eleccion

def index_candidatos(request):
    elecciones = Eleccion.objects.all()
    return render(request, 'candidato/index.html', {"elecciones": elecciones})

def perfil_candidato(request, idc):
    candidato = get_object_or_404(Candidato, pk=idc)
    return render(request, 'candidato/perfil.html', {"candidato":candidato})

