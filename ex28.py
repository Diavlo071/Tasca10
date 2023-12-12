def bintodec (bin):
    return int(bin,2)

def llbintodec(llbin):
    lldec = []
    for i in llbin:
        lldec.append(bintodec(i))
    return lldec


#Programa principal

a = ["100", "01", "01","1000101"]
b = llbintodec(a)
for i, e in enumerate(b):
    print("El numero binari : ", a[i], " es correspon amb el numero decimal: ", e)
