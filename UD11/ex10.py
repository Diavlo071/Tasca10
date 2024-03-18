def div(a,b):
    try:
        c= a/b
        print("La divisio de {} entre {} es {}".format(a,b,c))
    except ZeroDivisionError:
        print("El segon parametre no pot ser zero")

#Programa Principal
a = int(input("Escriure el numerador: "))
b = int(input("Escriure el Denominador: "))

div(a,b)