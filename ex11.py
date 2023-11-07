#Calculadora
def menu_principal():
    print("""
        Menu Principal:
          1. Calculadora nombres Enters
          2. Calculadora nombres Reals 
          3. Sortir
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
            a = -1
        case other:
            print("Opcio no valida!")