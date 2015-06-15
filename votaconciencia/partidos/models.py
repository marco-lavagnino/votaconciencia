from django.db import models
from colorful.fields import RGBColorField
from django.core.urlresolvers import reverse


class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    abreviacion = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True)
    color = RGBColorField()
    informacion = models.TextField(null=True, blank=True)
    alianza = models.ForeignKey('Alianza', related_name='partidos', null=True, blank=True)

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('partidos.views.perfil_partido', args=[str(self.id)])


class Alianza(models.Model):
    nombre = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=30)
    logo = models.ImageField(null=True, blank=True)
    color = RGBColorField()
    informacion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Alianza"
        verbose_name_plural = "Alianzas"

    def __unicode__(self):
        return self.nombre
