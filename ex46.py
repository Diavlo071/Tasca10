#Aqui compara si esta ordenada la llista
def  esta_ordenada(a):
	b = a.copy()
	c = a.copy()
	b.sort()
	c.sort(reverse=True)
	if a == b:
		print("La llista {} està ordenada ascendentment {}".format(a, b))
	elif a==c:
		print("La llista {} està ordenada descendentment {}".format(a, c))
	else:
		print("La llista {} no està ordenada {}".format(a, b))
#Llegeix la llista
def llegir_llista():
	a=[]
	c="a"
	while c!=".":
		c=input("Introdueixi un element de la llista i punt (.) per acabar: ")
		if c!=".":
			a.append(c)
	return a
#Pprincipal
a = llegir_llista()
esta_ordenada(a)
