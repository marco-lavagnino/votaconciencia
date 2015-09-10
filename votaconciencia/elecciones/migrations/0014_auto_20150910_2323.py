# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0013_remove_postulacion_eleccion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['-id'], 'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
    ]
