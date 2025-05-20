vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"

def elimina_vocala(ch):
    return ch not in vocale

#print(list(filter(elimina_vocala, input_string)))
#varianta1
print("".join(filter(elimina_vocala, input_string)))

#varianta2
print("".join(filter(lambda x:x not in vocale, input_string)))

#list comprehension
print("".join([ch for ch in input_string if ch not in vocale]))