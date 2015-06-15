from django.db import models
from django.core.urlresolvers import reverse


class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(null=True, blank=True)
    bio = models.TextField()
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    pagina_personal = models.URLField(null=True)
    boleta = models.ImageField(null=True, blank=True)
    partido = models.ForeignKey('partidos.Partido', related_name='candidatos')
    eleccion = models.ForeignKey('elecciones.Eleccion', related_name='candidatos')

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('candidatos.views.perfil_candidato', args=[str(self.id)])

class Propuesta(models.Model):
    candidato = models.ForeignKey('Candidato', related_name='propuestas')
    descripcion = models.TextField()
    cumplida = models.BooleanField(default = False)

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"

    def __unicode__(self):
        return "propuesta de " + self.candidato.nombre