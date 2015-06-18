# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('informacion', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Eleccion',
                'verbose_name_plural': 'Elecciones',
            },
            bases=(models.Model,),
        ),
    ]
