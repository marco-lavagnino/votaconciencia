# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0003_candidato_spot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='eleccion',
            field=models.ForeignKey(to='elecciones.Eleccion'),
            preserve_default=True,
        ),
    ]
