# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0004_auto_20150905_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleccion',
            name='popup',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
