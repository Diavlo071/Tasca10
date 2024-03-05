#Aquesta funcio se encarega de agafar de una llista la paraula mes gran
def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
#I aquesta es la Llista
x = ["Hola", "IES", "Joan", "Ramis"]
print("\nLa paraula mes gran es: ", paraula_mes_gran(x))

