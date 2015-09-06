# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def forwards(apps, schema_editor):
    Eleccion = apps.get_model('elecciones', 'Eleccion')
    Cargo = apps.get_model('elecciones', 'Cargo')
    Postulacion = apps.get_model('elecciones', 'Postulacion')
    # Crear cargos
    cargo_legislador = Cargo.objects.create(nombre="legislador")
    for e in Eleccion.objects.all():
        try:
            cargo_eleccion = Cargo.objects.get(nombre__iexact=e.titulo_en_juego)
        except Cargo.DoesNotExist:
            cargo_eleccion = Cargo.objects.create(nombre=e.titulo_en_juego)
        for c in e.candidatos.all():
            p = Postulacion()
            p.candidato = c
            p.cargo = cargo_eleccion if not c.legislador else cargo_legislador
            p.eleccion = e
            p.save()


def backwards(apps, schema_editor):
    Cargo = apps.get_model('elecciones', 'Cargo')
    Postulacion = apps.get_model('elecciones', 'Postulacion')
    Cargo.objects.all().delete()
    Postulacion.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0007_cargo_postulacion'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
