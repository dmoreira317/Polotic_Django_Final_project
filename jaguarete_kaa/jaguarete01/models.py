from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Producto(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    categoria_base = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    detalle = models.CharField(max_length=1000, default='N/A')
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='uploaded_images')
    fecha_creacion = models.DateTimeField()

    def __str__(self):
        return self.titulo

    def id(self):
        return reverse("jaguarete01:producto", kwargs={
            'pk' : self.pk
        })
    def agregar_carrito(self):
        return reverse("jaguarete01:agregar_carrito", kwargs={
            'pk' : self.pk
        })
    def sacar_carrito(self):
        return reverse("jaguarete01:sacar_carrito", kwargs={
            'pk' : self.pk
        })
    def mostrar_imagen(self):
        with open(self.imagen.path) as fp:
            return fp.read().replace('\n', '<br>')

class ProductoAgregado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ya_agregado = models.BooleanField(default=False)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} of {self.producto.titulo}"

    def precio_total_producto(self):
        return self.cantidad * self.producto.precio


class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(ProductoAgregado)
    fecha = models.DateTimeField(auto_now_add=True)
    ya_pedido = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username

    def precio_total_carrito(self):
        total = 0
        for producto in self.productos.all():
            total += producto.precio_total_producto()
        return total