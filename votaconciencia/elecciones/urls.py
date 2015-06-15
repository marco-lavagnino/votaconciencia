# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from elecciones import views

urlpatterns = patterns('',
    # urls de elecciones
    url(r'(?P<id>\d+)/info', views.eleccion_informacion, name='eleccion_informacion'),
    url(r'(?P<id>\d+)/candidatos', views.eleccion_candidatos, name='eleccion_candidatos'),
    url(r'(?P<id>\d+)', views.eleccion_intermedio, name='eleccion_intermedio'),
    url(r'$', views.index_elecciones , name='elecciones'),
)

