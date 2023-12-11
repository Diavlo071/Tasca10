def gran_de_tres(a,b,c):

    if a > b > c:    
        print("El nombre {} es major que {} i {}".format(a,b,c))
    
    elif a > c > b:
        print("El nombre {} es major que {} i {}".format(a,c,b))
    elif b > c > a:
        print("El nombre {} es major que {} i {}".format(b,c,a))
    elif b > a > c:
        print("El nombre {} es major que {} i {}".format(b,a,c))
    elif c > a > b:
        print("El nombre {} es major que {} i {}".format(c,a,b))

    elif c > b > a:
        print("El nombre {} es major que {} i {}".format(c,b,a))

    else:
        print(a)
        

#Programa principal

a = int(input("Introdueix el primer nombra: "))

b = int(input("Introdueix el Segon nombra: "))

c = int(input("Introdueix el Tercer nombra: "))

gran_de_tres(a,b,c)