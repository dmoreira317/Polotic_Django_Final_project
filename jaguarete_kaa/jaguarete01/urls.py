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

    
]