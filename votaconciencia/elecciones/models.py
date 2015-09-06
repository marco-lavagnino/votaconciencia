# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from entrevistas.models import EntrevistaCandidato, EntrevistaPersonalidad

class Eleccion(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    logo = models.ImageField(null=True, blank=True)
    titulo_en_juego = models.CharField(max_length=50, null=True, blank=True)
    informacion = models.TextField(null=True, blank=True)
    popup = models.TextField(null=True, blank=True)

    candidatos = models.ManyToManyField('candidatos.Candidato', related_name='elecciones')

    class Meta:
        verbose_name = "Eleccion"
        verbose_name_plural = "Elecciones"

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('elecciones.views.eleccion_candidatos', args=[str(self.id)])

    def entrevistas(self):
        entrevistas_candidatos = list(EntrevistaCandidato.objects.filter(entrevistado__elecciones__id=self.id))
        entrevistas_personalidades = list(EntrevistaPersonalidad.objects.filter(eleccion__id=self.id))
        entrevistas = entrevistas_candidatos + entrevistas_personalidades
        return sorted(entrevistas,key=lambda e: -e.id)
