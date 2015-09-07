from django.db import models
from django.core.urlresolvers import reverse
from re import search
from partidos.models import Alianza, Partido
from random import random


class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank=True)
    bio = models.TextField()
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    pagina_personal = models.URLField(null=True, blank=True)
    boleta = models.ImageField(null=True, blank=True)
    partido = models.ForeignKey('partidos.Partido', related_name='candidatos')
    alianza = models.ForeignKey('partidos.Alianza', related_name='candidatos', null=True, blank=True)
    spot = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __unicode__(self):
        return self.nombre

    def representa_a(self):
        return self.alianza if self.alianza else self.partido

    def cuenta_tw(self):
        s = search(r'.*twitter.com/(?P<handle>.*)', self.twitter)
        return s.group('handle') if s else None

    def titulo(self):
        return u'Candidato por ' + self.partido.nombre

    def get_absolute_url(self):
        return reverse('candidatos.views.perfil_candidato', args=[str(self.id)])

    def porcentaje(self, eleccion=None):
        if not eleccion:
            eleccion = self.eleccion
        postulaciones = Postulacion.objects.filter(eleccion__id=eleccion)
        mi_postulacion = postulaciones.get(candidato__id=self.id)



class Propuesta(models.Model):
    candidato = models.ForeignKey('Candidato', related_name='propuestas')
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"

    def __unicode__(self):
        return "propuesta de " + self.candidato.nombre