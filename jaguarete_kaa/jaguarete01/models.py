from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=40, unique=True)
    categoria = models.CharField(max_length=40)
    precio = models.FloatField()
    imagen = models.FileField()
    fecha_creacion = models.DateTimeField()
    



