# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FechaImportante)
class SumFecha(SummernoteModelAdmin):
    pass
