# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0005_auto_20150610_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleccion',
            name='informacion',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='informacion',
        ),
    ]
