from django.db import models


class Productos(models.Model):
    nombres = models.CharField(max_length=120, blank=False)
    apellidos = models.CharField(max_length=120, blank=False)
    cedula = models.IntegerField()
    marca = models.CharField(max_length=120)
    serie = models.CharField(max_length=120)
    tensor = models.IntegerField()
    conector_mecanico = models.IntegerField()
    etiqueta = models.IntegerField()
    cable = models.IntegerField()
    amarras = models.IntegerField()
    picotes = models.IntegerField()

    def full_name(self):
        return '%s %s' % (self.nombres, self.apellidos)
