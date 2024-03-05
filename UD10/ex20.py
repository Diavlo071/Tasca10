#Llelgim la llista
def llegir_llista():
    a='a'
    llista=[]
    while a != '.':
        a = input("Introdueix una Nombre a la llista: ")
        if a != '.':
            llista.append(int(a))
        else:
            return llista

#Aqui mira les dues llistes i les si tenen un element en comu surt true i si no false
def superposicio(llista1,llista2):
    if llista1 == llista2:
        print(True)
    else:
        print(False)

#Programa Principal
l = llegir_llista()
m = llegir_llista()

#superposicio(l,m)

c = superposicio(l,m)

if c == 0:
    print("Les dues llistes no tenen cap element en comú.")
else:
    print("Les llistes tenen ", c ," elements en comú")