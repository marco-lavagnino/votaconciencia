# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0002_candidato_legislador'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='spot',
            field=models.TextField(default=datetime.date(2015, 6, 26)),
            preserve_default=False,
        ),
    ]
