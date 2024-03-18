def coincideixen(llista):
    l=[]
    for i,e in enumerate(llista):
        if e == i:
            l.append(e)
    print("Els elements de la llista {}que coincideixen en la seva posicio son {}".format(llista,l))

    #Programa principal
    l = [3, 7, 2, 3, 4, 5, 6, 2]
    coincideixen(l)