def crear_repetits(a,b):
    c = b
    for i in range(a):
        b = b + c
    return b

#Programa principal

numero = int(input("Inserta el numero: "))
caracter = input("Inserta el caracter: ")
print(crear_repetits(numero, caracter))
