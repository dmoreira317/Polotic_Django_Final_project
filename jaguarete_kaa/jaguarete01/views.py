from django.shortcuts import render

# Create your views here.
def index(request):
    dictionary = {}
    return render(request, 'index.html', context=dictionary)