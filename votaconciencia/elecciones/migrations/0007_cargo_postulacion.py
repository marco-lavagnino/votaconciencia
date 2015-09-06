# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0005_auto_20150905_2123'),
        ('elecciones', '0006_eleccion_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postulacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votos', models.IntegerField(null=True)),
                ('candidato', models.ForeignKey(related_name='postulaciones', to='candidatos.Candidato')),
                ('cargo', models.ForeignKey(to='elecciones.Cargo')),
                ('eleccion', models.ForeignKey(related_name='postulaciones', to='elecciones.Eleccion')),
            ],
            options={
                'verbose_name': 'Postulaci\xf3n',
                'verbose_name_plural': 'Postulaciones',
            },
            bases=(models.Model,),
        ),
    ]
