from django.db import models

class QuienesSomos(models.Model):
    contenido = models.TextField()

    class Meta:
        verbose_name = "Quienes somos"
        verbose_name_plural = "Quienes somos"

    def __unicode__(self):
        return "Quienes Somos"

