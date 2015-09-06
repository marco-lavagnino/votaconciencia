# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0005_auto_20150905_2123'),
        ('elecciones', '0008_esquema_de_cargos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='legislador',
        ),
        migrations.AlterField(
            model_name='candidato',
            name='facebook',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidato',
            name='pagina_personal',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidato',
            name='twitter',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
