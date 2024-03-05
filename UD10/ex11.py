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
def binto(numero):
    return bin(numero)
def octto(numero):
    return oct(numero)
def hexto(numero):
    return hex(numero)
def decto(numero):
    return(numero)


def Calculadora_de_nombres_decimals_a_binari():
    
    print("Hem passat per la calculadora de reals")
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
                #x = int(input("Introdueix el nombre: "))
                #bina = (bin(x))
                #print ("\nEl nombre en binari es: ", bina)
                b = int(input("Introdueix el numero binari: "))
                o = octto(b)
                d = decto(b)
                h = hexto(b)
                print("El numero binari {} es: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
            case 2: #Octal
                #x = int(input("Introdueix el nombre: "))
                #hexa = (hex(x))
                #print ("\nEl nombre en hexadecimal es: ", hexa)
                o = int(input("Introdueix el numero octal: "))
                b = binto(o)
                d = decto(o)
                h = hexto(o)
                print("El numero octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            case 3: #Hexadecimal
                #x = int(input("Introdueix el nombre: "))
                #octa = (oct(x))
                #print ("\nEl nombre en octal es: ", octa)
                h = int(input("Introdueix el numero hexadecimal: "))
                o = octto(h)
                b = binto(h)
                d = decto(h)
                print("El numero Hexadecimal {} es: \n oct -> {} \n bin -> {} \n dec -> {}".format(h,o,b,d))
            case 4: #Decimal
                #x = int(input("Introdueix el nombre: "))
                #deci = ((x))
                #print ("\nEl nombre en octal es: ", octa)
                d = int(input("Introdueix el numero decimal: "))
                b = binto(d)
                o = octto(d)
                h = hexto(d)
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




#Funcions de canvis de base
def dectobin(numero):
    return bin(numero)
def dectooct(numero):
    return oct(numero)
def dectohex(numero):
    return hex(numero)