# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from partidos import views

urlpatterns = patterns('',
    # urls de partidos
    url(r'perfil/(?P<idp>\d+)', views.perfil_partido , name='perfil_partido'),
    url(r'$', views.index_partidos , name='partidos'),
)

