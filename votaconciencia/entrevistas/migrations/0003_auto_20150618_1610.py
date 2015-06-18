# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrevistas', '0002_auto_20150615_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalidad',
            name='titulo',
        ),
        migrations.AddField(
            model_name='personalidad',
            name='bio',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
