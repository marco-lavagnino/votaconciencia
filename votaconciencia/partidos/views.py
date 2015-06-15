from django.shortcuts import render, get_object_or_404
from models import *
from candidatos.models import Candidato


# VIEWS DE PARTIDOS
def index_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'partido/index.html',{"partidos":partidos})

def perfil_partido(request,idp):
    partido = get_object_or_404(Partido, pk=idp)
    return render(request, 'partido/perfil.html', {"partido":partido})

