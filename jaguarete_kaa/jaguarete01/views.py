from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import Producto, Carrito, ProductoAgregado
import pprint
import json
import random


# Create your views here.
def index(request):
    dictionary = {}
    return render(request, 'index.html', context=dictionary)

def acerca_de(request):
    dictionary={}
    return render(request, 'acerca_de.html', context=dictionary)

def sign_up_form(request):
    form = forms.SignUpForm() # class defined in forms.py
    dictionary = {"form": form}
    
    if request.method == "POST":
        form = forms.SignUpForm(request.POST) # creating a variable that receives the POST
        if form.is_valid(): 
            password = form.clean_password2()
            form.save()

            return redirect('resultado_registro/')
        else:
            print("Invalid form request")
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }    
    else:
        form = forms.SignUpForm()
    
    dictionary = {
            'form': form
            }    
    return render(request, "registro.html", context=dictionary)

def resultado_registro(request):
    dictionary = {}
    return render(request, "resultado_registro.html", context=dictionary)

def login_form(request):
    username = 'not logged in'
    user = request.user
    form = AuthenticationForm()
    dictionary = {
        'form': form
    }
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        request.session['username'] = username
                        login(request, user)
            print('form and session started')
            return redirect('resultado_login/')
        else:
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }
    else:
        form = AuthenticationForm()

    dictionary = {
    'object_list': user,
    'form': form,
    }
          
    return render(request, "login.html", context=dictionary)

def resultado_login(request):
    dictionary = {}
    return render(request, "resultado_login.html", context=dictionary)

@login_required(login_url='/login/')
def sign_out(request): # my logout view
    request.session.clear()
    logout(request)
    print("All sessions closed")
    return render(request, "logout.html")

class VistaProducto(DetailView):
    model = Producto
    template_name = "producto.html"

class VistaResumenCompra(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def traer(self, *args, **kwargs):
        try:
            compra = Carrito.objects.get(user=self.request.user, ya_pedido=False)
            context= {
                'objeto': compra
            }
            return render(self.request, 'resumen_compra.html')
        except ObjectDoesNotExist:
            messages.error(self.request, 'No tiene un carrito todavía')
            return redirect('/')

@login_required(login_url= '/login/')
def agregar_al_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto_agregado, creado = ProductoAgregado.objects.get_or_create(
        producto = producto,
        usuario = request.user,
        ya_agregado = False
    )

    producto_existente_carrito = Carrito.objects.filter(user=request.user, ya_pedido=False)

    if producto_existente_carrito.exists():
        agrega_producto = producto_existente_carrito[0]

        if agrega_producto.items.filter(producto__pk=producto.pk).exists():
            producto_agregado.cantidad += 1
            producto_agregado.save()
            messages.info(request, "Agregada/s unidad/es")
            return redirect("jaguarete01:resumen_compra")
        else:
            agrega_producto.items.add(producto)
            messages.info(request, 'Producto agregado al carrito')
    else:
        fecha_pedido = timezone.now()
        agregado_al_pedido = Carrito.objects.create(usuario=request.user, fecha=fecha_pedido)
        agregado_al_pedido.items.add(producto)
        messages.info(request, "Producto agregado al carrito")
        return redirect('jaguarete01:resumen_compra')


@login_required
def quitar_del_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk )
    producto_existente = Carrito.objects.filter(
        usuario=request.user, 
        ya_pedido=False
    )
    if producto_existente.exists():
        quita_producto = producto_existente[0]
        if quita_producto.items.filter(producto__pk=producto.pk).exists():
            producto_en_lista = ProductoAgregado.objects.filter(
                producto=producto,
                usuario=request.user,
                ya_agregado=False
            )[0]
            producto_en_lista.delete()
            messages.info(request, "Item \""+producto_en_lista.item.item_name+"\" retirado del carrito")
            return redirect("jaguarete01:resumen_compra")
        else:
            messages.info(request, "Este producto no está en su carrito")
            return redirect("jaguarete01:producto", pk=pk)
    else:
        #add message doesnt have order
        messages.info(request, "No tiene un carrito")
        return redirect("jaguarete01:producto", pk = pk)


@login_required
def reducir_cantidad_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk )
    producto_existente = Carrito.objects.filter(
        usuario = request.user, 
        ya_pedido = False
    )
    if producto_existente.exists():
        quita_producto = producto_existente[0]
        if quita_producto.items.filter(producto__pk=producto.pk).exists() :
            item = ProductoAgregado.objects.filter(
                producto = producto,
                usuario = request.user,
                ya_agregado = False
            )[0]
            if item.cantidad > 1:
                item.cantidad -= 1
                item.save()
            else:
                item.delete()
            messages.info(request, "La cantidad fue modificada")
            return redirect("jaguarete01:resumen_compra")
        else:
            messages.info(request, "Este item no esta en su lista")
            return redirect("jaguarete01:resumen_compra")
    else:
        #add message doesnt have order
        messages.info(request, "No tiene un carrito")
        return redirect("jaguarete01:resumen_compra")
