# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from entrevistas import views

urlpatterns = patterns('',
    url(r'(?P<id>\d+)', views.entrevista_individual, name='entrevista_individual'),
    url(r'$', views.index_entrevistas , name='entrevista'),
)
