# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import elecciones
import django_summernote

urlpatterns = patterns('',
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^elecciones/', include('elecciones.urls')),
    url(r'^entrevistas/', include('entrevistas.urls')),
    url(r'^calendario/', include('calendario.urls')),
    url(r'^candidatos/', include('candidatos.urls')),
    url(r'^partidos/', include('partidos.urls')),
    url(r'^', include('general.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
