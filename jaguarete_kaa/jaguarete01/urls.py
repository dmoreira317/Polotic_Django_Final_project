# from jaguarete_kaa.jaguarete01.views import VistaProducto, VistaResumenCompra
from django.conf.urls import url
from django.urls import path
from jaguarete01 import views
from django.contrib.auth import views as auth_views


app_name = 'jaguarete01'

urlpatterns = [
    # marvelapp pages
    path("index/", views.index, name = "index"),
    path("acerca_de/", views.acerca_de, name="acerca_de"),
    path("registro/", views.sign_up_form, name = "sign_up_form"),
    path("registro/resultado_registro/", views.resultado_registro, name = "resultado_registro"),
    path("login/", views.login_form, name = "login"),
    path("login/resultado_login/", views.resultado_login, name = "resultado_login"),
    path("logout/", views.sign_out, name = "logout"),
   
    path('producto/<pk>/', views.VistaProducto.as_view(), name='producto'),
    path('resumen_compra', views.VistaResumenCompra, name='resumen_compra'),
    path('agregar_al_carrito/<pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar_del_carrito/<pk>/', views.quitar_del_carrito, name='quitar_del_carrito'),
    path('reducir_cantidad_producto/<pk>/', views.reducir_cantidad_producto, name='reducir_cantidad_producto')
    
]