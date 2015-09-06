# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0008_esquema_de_cargos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleccion',
            name='candidatos',
        ),
        migrations.RemoveField(
            model_name='eleccion',
            name='titulo_en_juego',
        ),
        migrations.AlterField(
            model_name='postulacion',
            name='votos',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
