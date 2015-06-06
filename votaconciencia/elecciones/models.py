from django.db import models


class Candidato(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField()
    bio = models.TextField()
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)
    pagina_personal = models.URLField(null=True)
    boleta = models.ImageField(null=True)
    partido = models.ForeignKey('Partido')
    eleccion = models.ForeignKey('Eleccion')

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    abreviacion = models.CharField(max_length=30)
    logo = models.ImageField()
    color = models.CharField(max_length=6)

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"

    def __str__(self):
        return self.nombre

class Propuesta(models.Model):
    candidato = models.ForeignKey('Candidato')
    descripcion = models.TextField()
    cumplida = models.BooleanField(default = False)

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"

    def __str__(self):
        return "propuesta de " + self.candidato.nombre

class Eleccion(models.Model):
    nombre = models.CharField(max_length=40)
    terminada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Eleccion"
        verbose_name_plural = "Elecciones"

    def __str__(self):
        return self.nombre

