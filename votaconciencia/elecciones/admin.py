# -*- encoding: utf-8 -*-
from django.contrib import admin
from django import forms
from models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.admin import SummernoteModelAdmin


class InlineCargo(admin.TabularInline):
    model = Cargo
    extra = 0

class EleccionForm(forms.ModelForm):
    class Meta:
        model = Eleccion
        exclude = []
        widgets = {
        'popup' : SummernoteInplaceWidget(attrs={'height':'150px'}),
        'informacion': SummernoteWidget(attrs={'height':'700px'}),
        }


@admin.register(Eleccion)
class SumEleccion(SummernoteModelAdmin):
    inlines = [InlineCargo]
    form = EleccionForm

