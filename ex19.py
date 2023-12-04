def es_palindrom():
    x = input("Introdueix la paraula que vols que comprovi si es palindrom  o no: ")

    if x == x[::-1]:
        print ("Es Palindrom")
    else:
        print ("No es Palindrom")

#Programa Principal

es_palindrom()