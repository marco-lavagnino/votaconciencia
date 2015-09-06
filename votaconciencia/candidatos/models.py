from django.db import models
from django.core.urlresolvers import reverse
from elecciones.models import Cargo
from re import search
from partidos.models import Alianza, Partido

class CandidatoQuerySet(models.QuerySet):
    def por_cargo(self):
        result = {}
        for values in self.values('postulaciones__cargo__nombre').distinct():
            cargo = Cargo.objects.get(nombre=values['postulaciones__cargo__nombre'])
            result[cargo] = self.filter(postulaciones__cargo=cargo)
        return result

    def por_representacion(self):
        result = {}

        for values in self.exclude(alianza__isnull=True).values('alianza').distinct():
            alianza_id = values['alianza']
            result[Alianza.objects.get(id=alianza_id)] = self.filter(alianza_id=alianza_id)

        for values in self.exclude(alianza__isnull=False).values('partido').distinct():
            partido_id = values['partido']
            result[Partido.objects.get(id=partido_id)] = self.filter(partido_id=partido_id)

        return result


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
    spot = models.TextField()

    objects = CandidatoQuerySet.as_manager()

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


class Propuesta(models.Model):
    candidato = models.ForeignKey('Candidato', related_name='propuestas')
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"

    def __unicode__(self):
        return "propuesta de " + self.candidato.nombre