from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def capitalizare_view(request, text):
    return HttpResponse(text.upper())
#merge .. un raspuns generic sa vedem ca functioneaza

def parametri_view(request):
    print(request.GET)
    primit = request.GET.get('text')
    print("Ai primit", primit)
    if primit:
        return HttpResponse(primit.upper())
    else:
        return HttpResponse("Nu am gasit un parametru text ... ")