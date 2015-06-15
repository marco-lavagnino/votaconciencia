# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FechaImportante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'fecha importante',
                'verbose_name_plural': 'fechas importantes',
            },
            bases=(models.Model,),
        ),
    ]
