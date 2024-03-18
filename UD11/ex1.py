def lenp(frase):
    r=frase.split(" ")
    l=list(map(len,r))
    print("La longitud de les paraules de la llista {} es {}".format(frase,l))

#Programa principal Ex1

frase = input("\nEscriu una Frase: ")
lenp(frase)