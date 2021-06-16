from django.shortcuts import render

# Create your views here.
def index(request):
    dictionary = {}
    return render(request, 'index.html', context=dictionary)

def acerca_de(request):
    dictionary={}
    return render(request, 'acerca_de.html', context=dictionary)