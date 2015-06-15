# -*- encoding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

class Eleccion(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    informacion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Eleccion"
        verbose_name_plural = "Elecciones"

    def __unicode__(self):
        return self.nombre


    def get_absolute_url(self):
        return reverse('elecciones.views.perfil_eleccion', args=[str(self.id)])
