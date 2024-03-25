''' #Programa p`rincipal
def menu():
    op = 0
    while op<1 or op>14:
        print("""
        Programa principal
        1.
        2.
        3.
        4.
        5.
        6.
        7.
        8.
        9.
        10.
        11.
        12.
        13.
        14. sortir
            """)
        op = int(input("Introudeix una opcio: "))
        if op<1 or op>14:
            print("oppcio no valida")
        else:
            return op

#Programa principal
op=1
while op!=14:
    op = menu()
    match(op):
        case 1:
            ex1()
        case 6:
            l=['hola','si']
            c = "h"

            case 14:
        


'''

'''def ex1():
    a = int(input("Introudeix el Primer nombre: "))
    b = int(input("Introudeix el Segon nombre: "))
    if a>b:
        print("{} es major que{}".format(a,b))
    elif b>a:
        print("{} es major que{}".format(b,a))
    else:
        print("Son iguals")
'''

'''def ex2():
    c = input("Introdueix una vocal (a,e,i,o,u): ")
    match(c):
        case 'a':
            print("Has escirt una a")
        case 'e':
            print("Has escirt una e")
        case 'i':
            print("Has escirt una i")
        case 'o':
            print("Has escirt una o")
        case 'u':
            print("Has escirt una u")
        case other:
            print("no sha trobat cap vocal")
'''


'''def ex3():
    a = []
    b = []
    for i in range(3):
        a.append(input("Introdueix la paraula: "))
        for e in a:
            b.append(len(e))
        print("Les longituds de la llista {} son {}".format(a,b))

'''

'''def ex4():
    for i in range(1,10,2):
        print(i)

'''


'''def ex5():
    a = [1, 2, 3, 4, 5] 
    d = {}
    for i,e in enumerate(a):
        d[i]=e
    print(d)
'''


'''def ex6(l,c):
    b=[]
    for e in l:
        if c in e:
            b.append(e)
    print("De la llista {}, les seguents {} contenen el caracter {}".format(l.b.c))
'''
            

'''def ex7():
    a = [3,4,6,8,9]
    b = list(map(lambda x: x+10, a))
    print(b)
'''

'''def ex8 ():
    a = [3,4,6,8,9]
    b = [e**2 for e in a if e%2==1]
    print(b)
'''

'''def ex9():
    a = ["Piano","Bateria","Clarinet","Saxo","Cello"]
    b = list(map(lambda x: x [::-1],a))
    print(b)
'''

'''def ex10():
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    c = list(zip(a,b))
    print(c)
'''

'''def ex11():
    a = [1,2,3,4,5]
    b = list(filter(lambda x: x%2==1,a))
    print(b)
'''

'''class Ordinador():
    def __init__(self, tipus , pantalla):
        self.tipus=tipus
        self.pantalla=pantalla
    def GetTipus(self):
        print(self.tipus)
    def Getpantalla(self):
        print(self.pantalla)
'''

'''def ex13():
    with open("/home/cicles/AO/ex20.txt","w") as f:
        for i in range(10):
            f.write(i+"\n")
    with open("home/cicles/AO/ex20.txt", "r") as f:
        for i in f:
            print(i)
'''