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
            field=models.ForeignKey(related_name=b'entrevistas', to='candidatos.Candidato'),
        ),
        migrations.AlterField(
            model_name='entrevistapersonalidad',
            name='entrevistado',
            field=models.ForeignKey(related_name=b'entrevistas', to='entrevistas.Personalidad'),
        ),
    ]
