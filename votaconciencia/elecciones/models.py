# -*- encoding: utf-8 -*-

from django.db import models
from colorful.fields import RGBColorField

class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank=True)
    bio = models.TextField()
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    pagina_personal = models.URLField(null=True)
    boleta = models.ImageField(null=True, blank=True)
    partido = models.ForeignKey('Partido', related_name='candidatos')
    eleccion = models.ForeignKey('Eleccion', related_name='candidatos')

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __unicode__(self):
        return self.nombre

class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    abreviacion = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True)
    color = RGBColorField()
    informacion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"

    def __unicode__(self):
        return self.nombre

class Propuesta(models.Model):
    candidato = models.ForeignKey('Candidato', related_name='propuestas')
    descripcion = models.TextField()
    cumplida = models.BooleanField(default = False)

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"

    def __unicode__(self):
        return "propuesta de " + self.candidato.nombre

class Eleccion(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    informacion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Eleccion"
        verbose_name_plural = "Elecciones"

    def __unicode__(self):
        return self.nombre

class FechaImportante(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "fecha importante"
        verbose_name_plural = "fechas importantes"

    def __unicode__(self):
        return self.titulo

