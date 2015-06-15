# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0008_auto_20150613_1459'),
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
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='partido',
            name='alianza',
            field=models.ForeignKey(related_name='partidos', blank=True, to='elecciones.Alianza', null=True),
            preserve_default=True,
        ),
    ]
