#def major()

#def intercanvi(a,b):
#    return b,a
#
#x= int(input("Introdueix el primero nombre: "))
#y= int(input("Introdueix el Segon nombre: "))

#print("\nEl valor d'x es {} i el de y es {}\n".format(x,y))
#x,y = intercanvi(x,y)
#print("\nDespres del intecanvi el valor de x es {} i el de y es {}".format(x,y))

def major(x,y):
    if x>y:
        return x
    else:
        return y
    
ne= int(input("Introdueix el primero nombre: "))
nu= int(input("Introdueix el Segon nombre: "))
z = major(ne,nu)
print("El major de {} i {} es {}".format(ne,nu,z))