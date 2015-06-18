# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='legislador',
            field=models.BooleanField(default=False, verbose_name=b'es candidato a legislador?'),
            preserve_default=True,
        ),
    ]
