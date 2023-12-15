#Funcio li deim que si es major de 18 print Ets Major de 18 anys i si no Ets Menor de 18 anys i si tens 18 manys "Tens 18 anys"

def major(a):
    if a>18:
        print("Ets Major de 18 anys.")
    elif a<18:
        print("Ets Menor de 18 anys.")
    else:
        print("Tens 18 anys.")

#Programa Principal

Edad = int(input("Intodueix la seva edad: "))
major(Edad)