def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
x = ["Hola", "IES", "Joan", "Ramis"]
print("\nLa paraula mes gran es: ", paraula_mes_gran(x))

