from random import random
import random
#Aqui fa una llista de 20 elements dels 1 al 100
def llista_20_elements():
	l = []
	for i in range(20):
		l.append(random.randint(1,100))
	return l
#Aqui compara si esta duplicat o no
def hi_ha_duplicats(a):
	seen = set()    
	dupes = [x for x in a if x in seen or seen.add(x)] 	 
	if len(dupes)>0:
		print("La llista {} té elements duplicats {}".format(a,dupes))
	else:
   		 print("La llista {} no té elements duplicats {}".format(a,dupes))
#Si esta duplicat una llista la elimina
def elimina_duplicats(a):
    b= list(set(a))
    return b

#Pprincipal
x = llista_20_elements()
hi_ha_duplicats(x)
y = elimina_duplicats(x)
y.sort()
print("Llavors, la llista sense elements duplicats és {}".format(y))
