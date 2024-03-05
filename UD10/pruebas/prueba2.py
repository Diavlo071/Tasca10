a = 1
while a>0:
    print("""
        Menu Principal:
          1. par o impar
          3. Sortir
    """)
    a = int(input('Elegexi una opcio: '))
    match a:
        case 1:
            b = int(input("Escriure un numero: "))
            if b % 2 == 0:
                    print("par")
            else:
                print("Inparell")
        case 2:
            a = 0
