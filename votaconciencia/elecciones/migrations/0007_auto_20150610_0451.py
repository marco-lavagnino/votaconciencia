# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0006_auto_20150610_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleccion',
            name='informacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='partido',
            name='informacion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
