# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0004_auto_20150905_2104'),
        ('entrevistas', '0002_auto_20150626_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrevistapersonalidad',
            name='eleccion',
            field=models.ForeignKey(default=3, to='elecciones.Eleccion'),
            preserve_default=False,
        ),
    ]
