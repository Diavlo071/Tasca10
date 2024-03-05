#Repeteix el nombre de vegades del nombre i el suma a el caracter

def crear_repetits(a,b):
    c = ''
    for i in range(a):
        c += b
    return c

#Programa principal

numero = int(input("Inserta el numero: "))
caracter = str(input("Inserta el caracter: "))
print(crear_repetits(numero, caracter))
