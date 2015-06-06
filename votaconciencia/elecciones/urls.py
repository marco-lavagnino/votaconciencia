from django.conf.urls import patterns, include, url
from elecciones import views

urlpatterns = patterns('',
    url(r'elecciones', views.index_elecciones , name='elecciones'),
    url(r'$', views.index , name='inicio'),
)

