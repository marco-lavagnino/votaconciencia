from django.conf.urls import patterns, include, url
from elecciones import views

urlpatterns = patterns('',
    # urls de partidos
    url(r'perfil_partidos/(?P<idp>\d+)', views.perfil_partido , name='partidos'),
    url(r'partidos', views.index_partidos , name='partidos2'),
    # urls de candidatos
    url(r'perfil/(?P<idc>\d+)', views.perfil_candidato , name='perfil'),
    url(r'candidatos', views.index_candidatos , name='candidatos'),
    # urls de elecciones
    url(r'eleccion/(?P<id>\d+)', views.perfil_eleccion, name='eleccion_individual'),
    url(r'elecciones', views.index_elecciones , name='elecciones'),
    # otras urls
    url(r'informacion^', views.informacion, name="info"),
    url(r'$^', views.index , name='inicio'),
)

