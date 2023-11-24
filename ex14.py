def gran_de_tres():

    if a > b and a > c:    
        print("El nombre {} es major que {} i {}".format(a,b,c))
    
    elif b > a and b > c:
        print("El nombre {} es major que {} i {}".format(b,a,c))
        
    else:
        print("El nombre {} es major que {} i {}".format(c,a,b))
        
    


#Programa principal

a = int(input("Introdueix el primer nombra: "))

b = int(input("Introdueix el Segon nombra: "))

c = int(input("Introdueix el Tercer nombra: "))

gran_de_tres()