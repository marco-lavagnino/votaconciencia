# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Candidato)
class SumCandidato(SummernoteModelAdmin):
    pass

@admin.register(Partido)
class SumPartido(SummernoteModelAdmin):
    pass

@admin.register(Eleccion)
class SumEleccion(SummernoteModelAdmin):
    pass

@admin.register(Propuesta)
class SumPropuesta(SummernoteModelAdmin):
    pass

