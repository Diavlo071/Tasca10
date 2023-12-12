#Aquesta funcio fa que ordeni la llista de menor a major i despues la inverteix
def gran_llista(e):
    e.sort()
    return e[::-1]

#Programa 

llista = [3,63,2,6,11,77,25,223]
l = gran_llista(llista)
# I aquifeim que agafi el primer valor de la llista invertida
print (l[0])
