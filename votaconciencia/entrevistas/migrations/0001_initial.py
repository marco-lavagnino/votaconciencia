# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrevista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', models.TextField()),
            ],
            options={
                'verbose_name': 'Entrevista',
                'verbose_name_plural': 'Entrevistas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntrevistaCandidato',
            fields=[
                ('entrevista_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='entrevistas.Entrevista')),
                ('entrevistado', models.ForeignKey(to='elecciones.Candidato')),
            ],
            options={
                'verbose_name': 'Entrevista a candidato',
                'verbose_name_plural': 'Entrevistas a candidatos',
            },
            bases=('entrevistas.entrevista',),
        ),
        migrations.CreateModel(
            name='EntrevistaPersonalidad',
            fields=[
                ('entrevista_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='entrevistas.Entrevista')),
            ],
            options={
                'verbose_name': 'Entrevista a personalidad',
                'verbose_name_plural': 'Entrevistas a personalidades',
            },
            bases=('entrevistas.entrevista',),
        ),
        migrations.CreateModel(
            name='Personalidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'')),
                ('nombre', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Personalidad',
                'verbose_name_plural': 'Personalidades',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entrevistapersonalidad',
            name='entrevistado',
            field=models.ForeignKey(to='entrevistas.Personalidad'),
            preserve_default=True,
        ),
    ]
