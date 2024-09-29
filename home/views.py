from django.shortcuts import render

# Create your views here.


def accueil(request):
    return render(request, 'home/accueil.html')

def equipe(request):
    return render(request, 'home/equipe.html')

def preferences(request):
    return render(request, 'home/preferences.html')

def revetements(request):
    return render(request, 'home/revetements.html')

def contact(request):
    return render(request, 'home/contact.html')