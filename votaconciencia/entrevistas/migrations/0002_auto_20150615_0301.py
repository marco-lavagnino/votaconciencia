# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrevistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevistacandidato',
            name='entrevistado',
            field=models.ForeignKey(to='candidatos.Candidato'),
            preserve_default=True,
        ),
    ]
