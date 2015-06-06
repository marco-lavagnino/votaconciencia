from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index (request):
    return render_to_response('home/index.html',ctx,
    context_instance=RequestContext(request)
    )
