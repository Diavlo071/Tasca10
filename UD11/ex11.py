def imprimir_fitxer(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
        print(a)
def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+"\n")

#Programa Principal
fitxer = "/home/joan/AO/Tasca10/UD11/ex11.txt"
llista = ["Jordi","Claudia","David","Ayub","Oscar","Paula","Sebas","Anas"]
afegir_fitxer(fitxer,llista)
imprimir_fitxer(fitxer)