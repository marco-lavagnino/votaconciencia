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
