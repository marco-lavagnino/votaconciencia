# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0011_eleccion_de_postulacion_a_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacion',
            name='cargo',
            field=models.ForeignKey(related_name='postulaciones', to='elecciones.Cargo'),
            preserve_default=True,
        ),
    ]
