from django.db import models

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=60)

class Producto(models.Model):
    titulo = models.CharField(max_length=40, unique=True)
    # categoria = models.ForeignKey()
    precio = models.FloatField()
    imagen = models.FileField()
    fecha_creacion = models.DateTimeField()

class Carrito():
    usuario = models.CharField()
    lista_productos = models.CharField()
    precio_total = models.FloatField()

    
