#a = int(input("Entra el Primer nombre: "))
#b = int(input("Entra el Segon nombre: "))
#c = int(input("Entra el Tercer nombre: "))

#if a >= b:
#    print("{} es major o igual que {}".format(a,b))
#else:
#    print("{} es menor que {}".format(a,b))
#a=[]
#f= int(input("Introdueix el tamany de la lista: "))
#for i in range(f):
#    b =input("""Que vols llegir
#             1. Numeros
#             2. ALtres: lletras,llistes,dicionaris
#             
#             """)
#    match b:
#        case "1":
#            a.append (int(input("Introdueix un numero: ")))
#        case other:
#            a.append (input("Introdueix un nou element: ")))
#print(a)


#INPORTANT
#a = [2, 3, 4]
#b = [5, 6, 10]
#a=b
#print(a)
#a[2]=15
#print(b)
##########

a = [2, 3, 4]
b = [2, 5, 6, 10]
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
print("La multiplicacio de la llista {} per la lllista {} es {}".format(a,b,c))

#a += b
#print(a)