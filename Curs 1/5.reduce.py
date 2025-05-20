from functools import reduce
culori = ["alb", "rosu", "negru", "verde"]

#ramane un singur element la reduce, nu mai e envoie sa transformam in lista. reduce are mereu 2 parametrii
print(reduce(lambda x, y: x if len(x)<len(y) else y, culori))