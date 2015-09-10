# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from entrevistas.models import EntrevistaCandidato, EntrevistaPersonalidad
from partidos.models import Alianza, Partido
from random import random
from django.db.models import F, Sum


class Eleccion(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    logo = models.ImageField(null=True, blank=True)
    informacion = models.TextField(null=True, blank=True)
    popup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Eleccion"
        verbose_name_plural = "Elecciones"

    def __unicode__(self):
        return u"%s (%d)" % (self.nombre, self.fecha.year)

    def get_absolute_url(self):
        return reverse('elecciones.views.eleccion_candidatos', args=[str(self.id)])

    def entrevistas_relacionadas(self):
        entrevistas_candidatos = list(EntrevistaCandidato.objects.filter(entrevistado__postulaciones__cargo__eleccion=self))
        entrevistas_personalidades = list(EntrevistaPersonalidad.objects.filter(eleccion__id=self.id))
        entrevistas = entrevistas_candidatos + entrevistas_personalidades
        return sorted(entrevistas,key=lambda e: -e.id)


class Cargo(models.Model):
    nombre = models.CharField(max_length=50)
    eleccion = models.ForeignKey(Eleccion, related_name='cargos')

    votos_en_blanco = models.IntegerField(null=True, blank=True)
    votos_nulos = models.IntegerField(null=True, blank=True)
    votos_impugnados = models.IntegerField(null=True, blank=True)

    CANDIDATO = 'Candidatos'
    PRECANDIDATO = 'Precandidatos'

    tipo_candidatura = models.CharField(max_length=50, choices=(
            (CANDIDATO, 'candidato'),
            (PRECANDIDATO, 'precandidato')
            ), default=CANDIDATO)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['-id']  # TODO: agregar un atributo de importancia, ordenar según eso.

    def __unicode__(self):
        return "%s en %s" % (self.nombre, self.eleccion)

    def votos_totales(self):
        votos_de_candidatos = self.postulaciones.aggregate(total=Sum('votos'))['total']
        votos_en_blanco = self.votos_en_blanco if self.votos_en_blanco else 0
        votos_nulos = self.votos_nulos if self.votos_nulos else 0
        votos_impugnados = self.votos_impugnados if self.votos_impugnados else 0
        return votos_de_candidatos + votos_en_blanco + votos_nulos + votos_impugnados

    def agrupar_por_representacion(self):
        result = {}

        for values in self.postulaciones.exclude(candidato__alianza__isnull=True).values('candidato__alianza').distinct():
            alianza_id = values['candidato__alianza']
            result[Alianza.objects.get(id=alianza_id)] = self.postulaciones.filter(candidato__alianza_id=alianza_id)

        for values in self.postulaciones.exclude(candidato__alianza__isnull=False).values('candidato__partido').distinct():
            partido_id = values['candidato__partido']
            result[Partido.objects.get(id=partido_id)] = self.postulaciones.filter(candidato__partido_id=partido_id)

        return sorted(result.items(), key=lambda x:random())


class Postulacion(models.Model):
    candidato = models.ForeignKey('candidatos.Candidato', related_name='postulaciones')
    cargo = models.ForeignKey(Cargo, related_name='postulaciones')

    votos = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"

    def __unicode__(self):
        return u"postulación de %s a %s" % (self.candidato.nombre, self.cargo)

