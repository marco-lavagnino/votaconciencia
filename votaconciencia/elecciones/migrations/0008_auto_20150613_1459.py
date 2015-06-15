# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0007_auto_20150610_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fechaimportante',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
