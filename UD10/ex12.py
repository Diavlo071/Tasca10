#Calculadora
def menu_principal():
    print("""
        Menu Principal:
          1. Calculadora nombres Enters.
          2. Calculadora nombres Reals.
          3. Calculadora de nombres bin,hexadecimal y octal.
          4. Sortir.
    """)
    a = int(input('Elegexi una opcio: '))
    return a
def calculadora_enters():
    print("Hem pasat per la calculadora d'enters")
    
    op = 1
    while op>0:
        print("""
            Menú enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
        op = int(input("Eligex una opcio: "))
        match op:
            case 1: # Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}".format(x, y, x+y))
            case 2: # Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x-y))
            case 3: # Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x*y))
            case 4:
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x/y))
            case 5:
                print("Tornar al menu \n\n")
                op=-1
    

def calculadora_reals():
    print("Hem passat per la calculadora de reals")

    op = 1
    while op>0:
        print("""
            Menú enters
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
        op = int(input("Eligex una opcio: "))
        match op:
            case 1: # Sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x+y))
            case 2: # Restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x-y))
            case 3: # Multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x*y))
            case 4:
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Introdueix el segon nombre: "))
                print("\n{} + {} = {}\n".format(x, y, x/y))
            case 5:
                print("Tornar al menu \n\n")
                op=-1

#Funcions de canvis de base
#De decimal a tots els altras
def dectobin(numero):
    #Prec: numero sigui un enter
    #Post: Retorna el valor de l'enter en binari
    return bin(numero)
def dectooct(numero):
    #Prec: numero sigui un enter
    #Post: Retorna el valor de l'enter en octal
    return oct(numero)
def dectohex(numero):
    #Prec: numero sigui un enter
    #Post: Retorna el valor de l'enter en hexadecimal
    return hex(numero)

#De binari a octal,decimal i hexadecimal
def bintooct(numero):
    #Prec: numero sigui una cadena de caracters i en binari 
    #Post Retorna el numero en octal
    a=int(str(numero),2)
    return dectooct(a)
def bintodec(numero):
    #Prec: numero sigui una cadena de caracters i en binari 
    #Post: Retorna el numero en decimal
    a=int(str(numero),2)
    return a
def bintohex(numero):
    #Prec: numero sigui una cadena de caracters i en binari 
    #Post: Retorna el numero en hexadecimal
    a=int(str(numero),2)
    return dectohex(a)

#Octal a binari , decimal i hexadecimal.
def octtobin(numero):
    #Prec: numero sigui una cadena de caracters i en octal
    #Post: Retorna el nombre el binari
    a=int(str(numero),8)
    return dectobin(a)
def octtodec(numero):
    #Prec: numero sigui una cadena de caracters i en octal
    #Post: Retorna el nombre el decimal
    a=int(str(numero),8)
    return a
def octtohex(numero):
    #Prec: numero sigui una cadena de caracters i en octal
    #Post: Retorna el nombre el hexadecimal
    a=int(str(numero),8)
    return dectohex(a)

#Hexadecimal a binari, octal i decimal 
def hextonum(hex):
    # Prec: hex és un caràcter
    # Post: retorna un valor enter
    pnum = {
            "f" : 15, 
            "e" : 14, 
            "d" : 13, 
            "c" : 12, 
            "b" : 11, 
            "a" : 10}
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)

def hextodec2(hex):
    # Prec: hex és una cadena de caràcters
    # Post: retorna el seu valor en decimal, número
    hex = hex.lower()
    hex = hex[:: -1]
    decimal = 0
    posicio = 0
    for digit in hex:
        Valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * Valor
        decimal += pnum
        posicio += 1
    return decimal
def hextobin(numero):
     # Prec: hex és una cadena de caràcters en hexadecimal
     # Post: retorna el número passat a binari
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
     # Prec: hex és una cadena de caràcters en hexadecimal
     # Post: retorna el número passat a octal   
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
     # Prec: hex és una cadena de caràcters en hexadecimal
     # Post: retorna el número passat a decimal  
    a = hextodec2(numero)
    return a
###

def Calculadora_de_nombres_decimals_a_binari():
    
    print("Hem passat per la calculadora de canvis de base")
    op = 1
    while op>0:
        print("""
            Menú enters
            1. Binari traduit tota la resta.
            2. Octal traduit tota la resta.
            3. Hexadecimal traduit tota la resta.
            4. Decimal traduit tota la resta.
            5. Sortir
        """)
        op = int(input("Eligex una opcio: "))
        match op:
            case 1: # Binari to

                b = int(input("Introdueix el numero binari: "))
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El numero binari {} es: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            case 2: #Octal

                o = int(input("Introdueix el numero octal: "))
                b = octtobin(o)
                d = octtodec(o)
                h = octtohex(o)
                print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            case 3: #Hexadecimal

                h = input("Introdueix el numero hexadecimal: ")
                o = hextooct(h)
                b = hextobin(h)
                d = hextodec(h)
                print("El numero Hexadecimal {} es: \n oct -> {} \n bin -> {} \n dec -> {}".format(h,o,b,d))
            case 4: #Decimal
                
                d = int(input("Introdueix el numero decimal: "))
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
                print("El numero Hexadecimal {} es: \n bin -> {} \n oct -> {} \n hex -> {}".format(h,o,b,d))
            case 5:
                print("Tornar al menu \n\n")
                op=-1


#Programa Principal

a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            Calculadora_de_nombres_decimals_a_binari()
        case 4:
            a = -1
        case other:
            print("Opcio no valida!")
