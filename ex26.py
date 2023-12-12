def filtrar_paraules(a, num):
        b = list()
        i = 0
        
        for e in a:
            if num < len(e):
                b.append(e)
        return b

llista = ["hola", "NO", "Ramis", "IES", "pepe", "Ironman"]
a = input("Indicar la longitud de les paraules que vols filtrar: ")
c = filtrar_paraules(llista,int(a))
print("Les paraules de igual o mes tamany de ", a, " son: ", c)

