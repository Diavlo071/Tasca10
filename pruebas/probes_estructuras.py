a = 'c'
if a == 'b':
    print("a es b")
elif a == 'c':
    print("a es c")
elif a == 'd':
    print("a es d")
elif a == 'e':
    print("a es e")
else:
    print("a no val res")

match a:
    case 'b':
        print("a es b")
    case 'c':
        print("a es c")
    case 'd':
        print("a es d")
    case 'e':
        print("a es e")
    case other:
        print("a no val res")

#a = [3, (1,3), [4,5,6], 7, "hola", '0',0, 1]

#if 'a' in a:
#    print("hola es dins la llista {}".format(a))
#elif 'holas' in a:
#    print("Hola es dins la llista {}".format(a))
#elif '0' in a:
#    print("Aixo se executa si es certa la condicio")
#elif 'b' in a:
#    print("b es dins {}".format(a))
#else:
#    print("Dins a hi ha {}".format(a))