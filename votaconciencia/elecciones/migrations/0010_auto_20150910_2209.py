# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elecciones', '0009_auto_20150906_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='eleccion',
            field=models.ForeignKey(related_name='cargos', default=1, to='elecciones.Eleccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cargo',
            name='tipo_candidatura',
            field=models.CharField(default=b'Candidatos', max_length=50, choices=[(b'Candidatos', b'candidato'), (b'Precandidatos', b'precandidato')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='votos_en_blanco',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='votos_impugnados',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cargo',
            name='votos_nulos',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
