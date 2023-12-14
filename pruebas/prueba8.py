l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1)
def Tercera_ocurrencia(l,e):
    a = l.count(e)
    if a==0:
        print("No halla ocurencies de aquest element")
    elif a==1:
        print("La primera ocurrencia de l' element esta en la posicio {}".format(l.index(e)))
        p = l.index(e)
        so = l.index(2,(p+1))
        print(so)   
    elif a>2:
        print("Hi ha mes de dues ocurrencia de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index(e,(so+1))
        print(to)
    else:
        print("Valor no Valid")

#Programa Principal
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1, 4, 2, 1)
x = int(input("Elegeix el element de la segona ocurrencia: "))
Tercera_ocurrencia(l,x)