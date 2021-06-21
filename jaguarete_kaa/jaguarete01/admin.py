from django.contrib import admin
from jaguarete01.models import Producto, ProductoAgregado,Carrito, Categoria

# Register your models here.

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ProductoAgregado)
admin.site.register(Categoria)
