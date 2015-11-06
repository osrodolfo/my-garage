from django.db import models
from django.utils import timezone


class Marca(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    usuario = models.ForeignKey('auth.User')
    correo = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca)
    modelo = models.IntegerField()
    descripcion = models.TextField()
    vendido = models.BooleanField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='static', blank = True)

    def __str__(self):
        return self.correo
