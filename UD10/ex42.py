#Aquie feim una funcio que fa que multipliqui per tots el serus nombres per treura la taula de multiplicar
def taula_multiplicar(a):
	for i in range(20):
		print("{} x {} = {}".format(i+1,a, (i+1)*a))
#Principal
#i Aqui li deim que introduesqui un valor
x = int(input("Introdueixi un número per a calcular la seva taula de multiplicar: "))
taula_multiplicar(x)
