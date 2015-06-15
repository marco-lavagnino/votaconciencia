# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alianza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('abreviacion', models.CharField(max_length=30)),
                ('logo', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('color', colorful.fields.RGBColorField()),
                ('informacion', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Alianza',
                'verbose_name_plural': 'Alianzas',
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
                ('informacion', models.TextField(null=True, blank=True)),
                ('alianza', models.ForeignKey(related_name='partidos', blank=True, to='partidos.Alianza', null=True)),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
            bases=(models.Model,),
        ),
    ]
