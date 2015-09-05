# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0004_auto_20150905_2103'),
        ('elecciones', '0002_eleccion_titulo_en_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleccion',
            name='candidatos',
            field=models.ManyToManyField(related_name='elecciones', to='candidatos.Candidato'),
            preserve_default=True,
        ),
    ]
