# -*- encoding: utf-8 -*-

from django.db import models
from elecciones.models import Candidato

class Personalidad(models.Model):
    foto = models.ImageField()
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Personalidad"
        verbose_name_plural = "Personalidades"

    def __unicode__(self):
        return self.nombre

class Entrevista(models.Model):
    entrevistado = ""
    contenido = models.TextField()

    class Meta:
        verbose_name = "Entrevista"
        verbose_name_plural = "Entrevistas"

    def __unicode__(self):
        return "entrevista a " + self.entrevistado.nombre

class EntrevistaCandidato(Entrevista):
    entrevistado = models.ForeignKey('elecciones.Candidato')

    class Meta:
        verbose_name = "Entrevista a candidato"
        verbose_name_plural = "Entrevistas a candidatos"

    def __unicode__(self):
        return "entrevista a " + self.entrevistado.nombre

class EntrevistaPersonalidad(Entrevista):
    entrevistado = models.ForeignKey('Personalidad')

    class Meta:
        verbose_name = "Entrevista a personalidad"
        verbose_name_plural = "Entrevistas a personalidades"

    def __unicode__(self):
        return "entrevista a " + self.entrevistado.nombre