# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0001_initial'),
        ('partidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('bio', models.TextField()),
                ('twitter', models.URLField(null=True)),
                ('facebook', models.URLField(null=True)),
                ('pagina_personal', models.URLField(null=True)),
                ('boleta', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('alianza', models.ForeignKey(related_name='candidatos', blank=True, to='partidos.Alianza', null=True)),
                ('eleccion', models.ForeignKey(related_name='candidatos', to='elecciones.Eleccion')),
                ('partido', models.ForeignKey(related_name='candidatos', to='partidos.Partido')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('cumplida', models.BooleanField(default=False)),
                ('candidato', models.ForeignKey(related_name='propuestas', to='candidatos.Candidato')),
            ],
            options={
                'verbose_name': 'Propuesta',
                'verbose_name_plural': 'Propuestas',
            },
            bases=(models.Model,),
        ),
    ]
