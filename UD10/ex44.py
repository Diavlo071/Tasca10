suma=0
#Introdueix  un valor
a = input("Introdueix un número: ")
#Aqui te diu el nombre i els digits
print("{} té {} dígits".format(a,len(a)))
for i,e in enumerate(a):
	if i%2==0:
    		print("El número parell {} és {}".format(i,e))