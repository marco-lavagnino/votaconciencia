# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from calendario import views

urlpatterns = patterns('',
    url(r'ajax', views.calendario_eventos, name="calendario_eventos"),
    url(r'$', views.calendario, name="calendario"),
)

