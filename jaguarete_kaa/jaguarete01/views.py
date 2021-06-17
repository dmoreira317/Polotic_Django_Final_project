from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
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