culori = ["alb", "rosu", "negru", "verde"]
def lungime_5(cuvant):
    return len(cuvant) == 5
print(list(filter(lungime_5, culori)))

#print(list(filter(lambda cuvant: len(cuvant) == 4, culori)))
print(list(filter(lambda x: len(x) == 4, culori)))

#concatenare
print(map(lambda x: x + x, culori))
print(list(map(lambda x: x + x, culori)))