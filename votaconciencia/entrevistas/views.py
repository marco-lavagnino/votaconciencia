from django.shortcuts import render, get_object_or_404
from models import *

# Create your views here.

def index_entrevistas (request):
    entrevistas = Entrevista.objects.all()
    return render(request, "entrevistas/index.html", entrevistas)

def entrevista_individual (request, id):
    entrevista = get_object_or_404(Entrevista, id=id)
    return render(request, "entrevistas/individual.html", {'entrevista':entrevista})
