# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0004_auto_20150610_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleccion',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 6, 10, 4, 44, 49, 847784, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eleccion',
            name='informacion',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
