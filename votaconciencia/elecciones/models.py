# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from entrevistas.models import EntrevistaCandidato, EntrevistaPersonalidad

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

    def entrevistas(self):
        entrevistas_candidatos = list(EntrevistaCandidato.objects.filter(entrevistado__postulaciones__eleccion__id=self.id))
        entrevistas_personalidades = list(EntrevistaPersonalidad.objects.filter(eleccion__id=self.id))
        entrevistas = entrevistas_candidatos + entrevistas_personalidades
        return sorted(entrevistas,key=lambda e: -e.id)


class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __unicode__(self):
        return self.nombre

class Postulacion(models.Model):
    candidato = models.ForeignKey('candidatos.Candidato', related_name='postulaciones')
    cargo = models.ForeignKey(Cargo)
    eleccion = models.ForeignKey(Eleccion, related_name='postulaciones')

    votos = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"

    def __unicode__(self):
        return u"postulación de %s a %s en %s" % (self.candidato.nombre, self.cargo.nombre, self.eleccion.nombre)
