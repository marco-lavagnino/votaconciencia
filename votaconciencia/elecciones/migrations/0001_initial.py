# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
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
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('informacion', models.TextField()),
            ],
            options={
                'verbose_name': 'Eleccion',
                'verbose_name_plural': 'Elecciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FechaImportante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'fecha importante',
                'verbose_name_plural': 'fechas importantes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('abreviacion', models.CharField(max_length=30)),
                ('logo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('color', colorful.fields.RGBColorField()),
                ('informacion', models.TextField()),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('cumplida', models.BooleanField(default=False)),
                ('candidato', models.ForeignKey(related_name='propuestas', to='elecciones.Candidato')),
            ],
            options={
                'verbose_name': 'Propuesta',
                'verbose_name_plural': 'Propuestas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='candidato',
            name='eleccion',
            field=models.ForeignKey(related_name='candidatos', to='elecciones.Eleccion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidato',
            name='partido',
            field=models.ForeignKey(related_name='candidatos', to='elecciones.Partido'),
            preserve_default=True,
        ),
    ]
