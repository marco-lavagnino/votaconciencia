# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0014_auto_20150910_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleccion',
            name='es_ballotage',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
