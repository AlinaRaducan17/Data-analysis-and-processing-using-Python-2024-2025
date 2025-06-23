from django.test import TestCase
import pycountry

# Create your tests here.

italia = pycountry.countries.get(alpha_2='IT')
print(italia.flag)


formatie =[('Dida', 'BR'), ('Oddo','IT'), ('Nesta', 'IT'), ('Maldini','IT'), ('Junkalovski','CZ'), ('Gattuso','IT'), ('Pirlo','IT'), ('Ambrosini','IT'), ('Kaka','BR'), ('Inzaghi','IT'), ('Seedors','NL')]

formatie = [(j, pycountry.countries.get(alpha_2=n).flag) for j,n in formatie]

pozitionare = [1, 4, 3, 2]

pozitionare_formatie =[]

counter = 0 
for i in pozitionare:
    pozitionare_formatie.append(formatie[counter: counter + i])
    counter += i
    print(formatie)