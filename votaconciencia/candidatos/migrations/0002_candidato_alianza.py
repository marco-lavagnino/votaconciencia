# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partidos', '0001_initial'),
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='alianza',
            field=models.ForeignKey(related_name='candidatos', blank=True, to='partidos.Alianza', null=True),
            preserve_default=True,
        ),
    ]
