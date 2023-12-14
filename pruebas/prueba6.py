a = [2, 3, 4]
print(a)
for i in a:
    resultat = a*2*2*2
    print(resultat)
print(a)
for i in range(len(a)):
    a [i]=a[i]*a[i]*a[i]
print(a)
for i, e in enumerate(a):
    a[i]=e*e*e
print(a)