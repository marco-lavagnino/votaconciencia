# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0006_auto_20150906_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='spot',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
