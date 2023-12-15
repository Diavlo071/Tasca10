suma=0
#Introdueixi un valor 
a = input("Introdueix un número: ")
#Aqui li diu que digi quin nombre as ficat i cuant de caracters te
print("{} té {} dígits".format(a,len(a)))
#Aqui les diu si es parrell o es sena
for i in a:
	suma = suma + int(i)
print("La suma dels dígits del número {} és {}".format(a,suma))
if suma%2==0:
	print("La suma dels dígits del número {} és parell".format(a))
else:
	print("La suma dels dígits del número {} és senar".format(a))
