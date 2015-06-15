from django.db import models


class FechaImportante(models.Model):
    fecha = models.DateField()
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "fecha importante"
        verbose_name_plural = "fechas importantes"

    def __unicode__(self):
        return self.titulo
