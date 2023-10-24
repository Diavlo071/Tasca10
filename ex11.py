def menu_principal():
    print("""
        Menu Principal:
          1. Calculadora Enters
          2. Calculadora  
          3. Sortir
          """)

    x = input("Elegexi una opcio: ")
    if x>0 and x<4:
        return x
    else:
        return 0

#match x:
#    case "":
#        print("")
#    case other

#Programa Principal

a = menu_principal():
print(a)