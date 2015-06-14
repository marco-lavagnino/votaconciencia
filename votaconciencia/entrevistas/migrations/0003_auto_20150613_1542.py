# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrevistas', '0002_auto_20150613_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntrevistaPersonalidad',
            fields=[
                ('entrevista_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='entrevistas.Entrevista')),
                ('entrevistado', models.ForeignKey(to='entrevistas.Personalidad')),
            ],
            options={
                'verbose_name': 'Entrevista a personalidad',
                'verbose_name_plural': 'Entrevistas a personalidades',
            },
            bases=('entrevistas.entrevista',),
        ),
        migrations.AlterModelOptions(
            name='entrevistacandidato',
            options={'verbose_name': 'Entrevista a candidato', 'verbose_name_plural': 'Entrevistas a candidatos'},
        ),
    ]
