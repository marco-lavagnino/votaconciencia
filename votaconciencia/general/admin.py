from django.contrib import admin
from models import *
from django_summernote.admin import SummernoteModelAdmin

@admin.register(QuienesSomos)
class SumQS(SummernoteModelAdmin):
    pass
