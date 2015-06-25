# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from general import views

urlpatterns = patterns('',
    url(r'quienes_somos/', views.quienes_somos , name='quienes_somos'),
    url(r'^$', views.index , name='inicio'),
)
