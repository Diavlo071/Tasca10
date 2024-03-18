from functools import reduce
def paraula_a_numeor(llista):
    a = list(map(lambda x:str(x), llista))
    b = reduce(lambda x,y:x+y, a)
    print("La llista {} es el numero {}".format(llista,b))

#Programa Principal
l=[3, 5, 7, 2, 1]
paraula_a_numeor(l)