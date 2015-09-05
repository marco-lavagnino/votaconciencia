# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def foreign_to_m2m(apps, schema_editor):
    Eleccion = apps.get_model('elecciones', 'Eleccion')
    for eleccion in Eleccion.objects.all():
        eleccion.candidatos = list(eleccion.candidato_set.all())

def backwards(apps, schema_editor):
    Eleccion = apps.get_model('elecciones', 'Eleccion')
    for eleccion in Eleccion.objects.all():
        eleccion.candidatos = []

class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0003_eleccion_candidatos'),
    ]

    operations = [
        migrations.RunPython(foreign_to_m2m, backwards),
    ]
