#Aqui demanam que intrudueixi un valor
x = int(input("Introdueixi un número natural (<100): "))
suma=0
#Aqui li deim que si 'i' esta entr el 1,'x',-4 i despre fa la operacio per veure si es menor que 100
for i in range(1,x,-4):
	suma = suma + (i**2)
print("La suma dels quadrats de 4 posicions menys de {} és {} ".format(x, suma))
