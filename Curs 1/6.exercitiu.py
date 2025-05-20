lista = [10, 2, 30, 50, 300, 10]

def elimina_elemente(element):
    return element > 5

#versiunea filter + functie
print(list(filter(elimina_elemente, lista)))

#versiunea filter + lambda
print(list(filter(lambda x: x > 5, lista)))

#versiunea list comprehension
print([element for element in lista if element > 5])
