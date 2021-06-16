from django.conf.urls import url
from django.urls import path
from jaguarete01 import views
from django.contrib.auth import views as auth_views

app_name = 'jaguarete01'

urlpatterns = [
    # marvelapp pages
    path("index/", views.index, name = "index"),
    path("acerca_de/", views.acerca_de, name="acerca_de")
]