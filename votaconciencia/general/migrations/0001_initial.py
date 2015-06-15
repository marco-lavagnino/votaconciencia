# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuienesSomos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', models.TextField()),
            ],
            options={
                'verbose_name': 'Quienes somos',
                'verbose_name_plural': 'Quienes somos',
            },
            bases=(models.Model,),
        ),
    ]
