from django.shortcuts import render
import pycountry

# Create your views here.

def formatie_2007_view(request):
 
    
    formatie =[('Dida', 'BR'), ('Oddo','IT'), ('Nesta', 'IT'), ('Maldini','IT'), ('Junkalovski','CZ'), ('Gattuso','IT'), ('Pirlo','IT'), ('Ambrosini','IT'), ('Kaka','BR'), ('Inzaghi','IT'), ('Seedors','NL')]
    
    pozitionare = [1, 4, 3, 2, 1]
    
    formatie = [(j, pycountry.countries.get(alpha_2=n).flag) for j,n in formatie]

    pozitionare_formatie =[]

    counter = 0 
    for i in pozitionare:
        pozitionare_formatie.append(formatie[counter: counter + i])
        counter += i
    
    context = {
        'linii': formatie,

    }
    return render(request, "2007.html", context)

def formatie_1994_view(request):
    return render(request, "fotbal.html")