# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from candidatos import views


urlpatterns = patterns('',
    # urls de candidatos
    url(r'perfil/(?P<idc>\d+)', views.perfil_candidato , name='perfil_candidato'),
    url(r'$', views.index_candidatos , name='candidatos'),
)
