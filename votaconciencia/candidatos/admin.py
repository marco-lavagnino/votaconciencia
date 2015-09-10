# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *
from django.db import models
from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from elecciones.models import Postulacion

class PostulacionInline(admin.StackedInline):
    model = Postulacion
    extra = 0

class SumPropuesta(admin.StackedInline):
    model = Propuesta
    extra = 0
    formfield_overrides = {
        models.TextField : {'widget':SummernoteInplaceWidget(attrs={'height':'200px'})}
    }

@admin.register(Candidato)
class SumCandidato(SummernoteModelAdmin):
    inlines = [
        PostulacionInline,
        SumPropuesta,
    ]

