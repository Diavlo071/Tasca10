def StringotoList(c):
    r=[x for x in c]
    print("De la cadena {} hem creat la llista {}".format(c,r))

#Programa Principal
c= input("Introdueix una paraula: ")
StringotoList(c)