# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0003_partido_informacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleccion',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='eleccion',
            name='informacion',
        ),
    ]
