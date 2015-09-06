# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0004_auto_20150905_2104'),
        ('candidatos', '0004_auto_20150905_2103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='eleccion',
        ),
        migrations.RemoveField(
            model_name='propuesta',
            name='cumplida',
        ),
    ]
