def crear_diccionari(llista):
    dic={}
    for i,e in enumerate(llista):
        dic[e]=i
    print("De la llista {} hem creat el dicionari {}".format(llista,dic))

    #Programa principal
    llista = ["Cotxe", "Casa", "Vaixell", "Colom", "Ca", "Mussol", "Clara"]
    crear_diccionari(llista)