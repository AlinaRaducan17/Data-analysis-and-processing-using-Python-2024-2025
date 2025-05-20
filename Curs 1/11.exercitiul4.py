from functools import reduce

#o functie care primeste o lista de nr ca argument si returneaza media acestora
lista = [10,2,30,50,300,10]

#versiunea1
print(sum(lista)/len(lista))

#versiunea2
print(reduce(lambda x, y: x+y, lista/len(lista)))

#versiunea3
print(reduce(lambda x, y: x+y, lista/reduce(lambda x,y:x+y, map(lambda x:1, lista))))