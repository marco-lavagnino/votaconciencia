from django.conf.urls import patterns, include, url
from elecciones import views

urlpatterns = patterns('',
    url(r'perfil/(?P<idc>\d+)', views.index_perfil , name='perfil'),
    url(r'candidatos', views.index_candidatos , name='candidatos'),
    url(r'elecciones', views.index_elecciones , name='elecciones'),
    url(r'eleccion/(?P<id>\d+)', views.eleccion_individual, name='eleccion_individual'),
    url(r'$^', views.index , name='inicio'),
)

