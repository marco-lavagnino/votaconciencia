# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0008_auto_20150613_1459'),
        ('entrevistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntrevistaCandidato',
            fields=[
                ('entrevista_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='entrevistas.Entrevista')),
                ('entrevistado', models.ForeignKey(to='elecciones.Candidato')),
            ],
            options={
                'verbose_name': 'Entrevista',
                'verbose_name_plural': 'Entrevistas',
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
                'verbose_name_plural': 'Personalidads',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='entrevista',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='entrevista',
            name='object_id',
        ),
        migrations.AddField(
            model_name='entrevista',
            name='contenido',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
