def filtar(llista, c):
    f=list(filter(lambda x: x[0]==c.lower() or x[0]==c.upper(), llista))
    print("De la llista {}, les paraulesque comencen per {} son {}".format(llista, c, f))

#Programa principal
llista = ["Josep","Joan","Jordi", "Maria", "Pera"]
c = "p"
filtar(llista,c)