#Repeteix el nombre de vegades del nombre i el suma a el caracter
def crear_repetits(a,b):
    c = ''
    for i in range(a):
        c += b
    return c
#I aquesta se encarega de transformalo a punts
def crear_punts(a,b):
    j=0
    for e in a:    
        for i in range(e):
                c= crear_repetits(b[j],'.')
                print(c)
        j+=1

#Programa Principal Per crear un dibuix
print ("Nave espacial\n")
a = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
b = [10,2,3,4,15,15,6,7,11,12,11,7,6,15,15,4,3,2,10]
crear_punts(a,b)
