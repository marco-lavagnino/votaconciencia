# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrevistas', '0002_auto_20150615_0301'),
        ('elecciones', '0009_auto_20150615_0111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='eleccion',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='partido',
        ),
        migrations.DeleteModel(
            name='FechaImportante',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='alianza',
        ),
        migrations.DeleteModel(
            name='Alianza',
        ),
        migrations.DeleteModel(
            name='Partido',
        ),
        migrations.RemoveField(
            model_name='propuesta',
            name='candidato',
        ),
        migrations.DeleteModel(
            name='Candidato',
        ),
        migrations.DeleteModel(
            name='Propuesta',
        ),
    ]
