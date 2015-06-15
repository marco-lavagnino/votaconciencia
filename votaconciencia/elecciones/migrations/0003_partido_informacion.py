# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0002_remove_partido_informacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='informacion',
            field=models.TextField(default='prueba'),
            preserve_default=False,
        ),
    ]
