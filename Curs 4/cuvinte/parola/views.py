from django.shortcuts import render
from django.http import HttpResponse

import random
import string
import pandas as pd

CIFRE = [str(i) for i in range(10)] #range(100) imi va da o parola din 100 cifre
LITERE_MARI = [chr(i) for i in range(ord('A'), ord('Z')+1)]
LITERE_MICI = [chr(i) for i in range(ord('a'), ord('z')+1)]



# Create your views here.
def random_view(request):
    
    OPTIUNI = CIFRE + LITERE_MARI + LITERE_MICI
    parola =""
    for i in range(100):
        parola += random.choice(OPTIUNI)
    
    return HttpResponse(parola)

OPTIONS = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

def alege_view(request):
    #GET - verb/metoda HTTP; get - metoda a dictionarului (nu da eroare)
    print(request.GET)
    context = {}
    
    lungime = request.GET.get('lungime')
    OPTIONS = string.ascii_lowercase
    if request.GET.get('withupper'):
        OPTIONS = string.ascii_uppercase
    if request.GET.get('withdigits'):
        OPTIONS += string.digits
    if request.GET.get('withspecial'):
        OPTIONS += string.punctuation
    
    
    print(lungime)
    try:
        lungime=int(lungime)
        parola =""
        for i in range(lungime):
            parola += random.choice(OPTIONS)
        context['parola'] = parola
        
    except:
        pass
    
    df = pd.read_csv("parole.csv")
    df.loc[len(df)] = parola
    df.to_csv("parole.csv")
    print(df)
    return render(request, "alege.html", context)