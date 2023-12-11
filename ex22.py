def crear_repetits(a,b):
    c = ''
    for i in range(a):
        c += b
    return c
def crear_punts(a,b):
    j=0
    for e in a:    
        for i in range(e):
                c= crear_repetits(b[j],'.')
                print(c)
        j+=1

#Programa Principal
a = [3,5,10,15,21]
b = [2,4,5,6,7,11]
crear_punts(a,b)