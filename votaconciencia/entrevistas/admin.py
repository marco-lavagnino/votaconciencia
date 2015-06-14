from django.contrib import admin
from models import *
from django_summernote.admin import SummernoteModelAdmin


@admin.register(EntrevistaCandidato)
class SumEntrevista(SummernoteModelAdmin):
    pass

@admin.register(EntrevistaPersonalidad)
class SumEntrevista(SummernoteModelAdmin):
    pass

@admin.register(Personalidad)
class SumEntrevista(SummernoteModelAdmin):
    pass