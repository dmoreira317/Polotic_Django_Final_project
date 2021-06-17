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

            return redirect('index/')
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