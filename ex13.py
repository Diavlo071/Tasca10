def retorna_major():

    if a > b:
        print("El nombre {} es major que {}".format(a,b))
    elif b > a:
        print("El nombre {} es major que {}".format(b,a))
    else:
        print("Els dos nombres son iguals")
    


#Programa principal

a = int(input("Introdueix el primer nombra: "))

b = int(input("Introdueix el Segon nombra: "))

retorna_major()