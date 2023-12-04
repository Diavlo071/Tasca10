def llegir_llista():
    a='a'
    llista=[]
    while a != '.':
        a = input("")
        if a != '.':
            llista.append(int(a))
        else:
            return llista

def sumar(llista):
    suma = 0
    for numero in llista:
        suma += numero
    return suma
    
    
def multiplicar(llista):
    Multiplicacio = 1
    for numero in llista:
        Multiplicacio *= numero
    return Multiplicacio


#Programa principal¡

l = llegir_llista()
print ("La suma de la llista {} es {}\n".format(l,sumar(l) ))

print ("La Multiplicacio de la llista {} es {}".format(l,multiplicar(l) ))


#sumar()
#multiplicar_llista()