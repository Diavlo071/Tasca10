#Definim la funcio
def Vocals_true():
    #Aqui feim que a igual els valors a,e,i,o,u el igualam a la variable perque cuant la introdueixis te digi es vocal 
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        print ("Si es Vocal Minusculas")
    #Aqui feim lo mateix que dalt pero amb caracter mayusculas
    elif a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
        print ("Si es Vocal Mayusculas")
    else:
        print ("No es vocal")

#Programa principal

a = input("\nIntrodueix una lletra: ")

Vocals_true()