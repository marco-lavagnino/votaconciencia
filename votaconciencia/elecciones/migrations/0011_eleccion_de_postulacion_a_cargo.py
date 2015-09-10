# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def forward(apps, schema_editor):
    Cargo = apps.get_model('elecciones', 'Cargo')
    Eleccion = apps.get_model('elecciones', 'Eleccion')
    Postulacion = apps.get_model('elecciones', 'Postulacion')
    for c in Cargo.objects.exclude(nombre__iexact='Presidente'):
        c.eleccion = c.postulacion_set.first().eleccion
        c.save()
    # Paso y nacionales
    paso = Eleccion.objects.get(nombre__iexact="paso")
    generales = Eleccion.objects.get(nombre__iexact="nacionales generales")
    candidato_presidente = Cargo.objects.create(nombre='presidente',eleccion=generales,tipo_candidatura='Candidatos')
    precandidato_presidente = Cargo.objects.create(nombre='presidente',eleccion=paso,tipo_candidatura='Precandidatos')
    for p in Postulacion.objects.filter(eleccion=paso):
        p.cargo = precandidato_presidente
        p.save()
    for p in Postulacion.objects.filter(eleccion=generales):
        p.cargo = candidato_presidente
        p.save()


def backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0010_auto_20150910_2209'),
    ]

    operations = [
        migrations.RunPython(forward, backward)
    ]
