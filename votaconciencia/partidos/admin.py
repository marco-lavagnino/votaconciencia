# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import *
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Partido)
class SumPartido(SummernoteModelAdmin):
    pass

@admin.register(Alianza)
class SumPartido(SummernoteModelAdmin):
    pass
