import os

llista=["1","2","3","4","5","6","7","8","9","10"]
os.chdir("/home/joan/AO/Tasca10/UD11/Examen_Tasca11/")
archi1=open("ex20.txt","w")

with open("ex20.txt","w") as f:
    print("Fitxer creat correctament!")
    for e in llista:
        f.write(e+"\n")

a = []
with open("ex20.txt","r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)