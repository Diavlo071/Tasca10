def llegir_llista():
    a='a'
    llista=[]
    while a != '.':
        a = input("Introdueix una Nombre a la llista: ")
        if a != '.':
            llista.append(int(a))
        else:
            return llista

def superposicio(llista1,llista2):
    if llista1 == llista2:
        print(True)
    else:
        print(False)

#Programa Principal

l = llegir_llista()
m = llegir_llista()

superposicio(l,m)

