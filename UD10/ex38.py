#Li demanam que introduiexi el valors seguents
x = float(input("Introdueixi la quantitat sol·licitada (50000 i 80000) euros: "))
y = float(input("Introdueixi l'interés (0.5 i 13) percentatge: "))
z = int(input("Introdueixi el número d'anys: "))
#Aqui feim la operacio
cfinal = x * (1 + y/100)**z
#I aqui retronam els resultats
print("El capital {}€ a un interés del {}% a {} anys resulta que pagarem {:.2f}€".format(x, y, z, cfinal))
