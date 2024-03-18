import os

companys=["Jordi","Claudia","Clara","Paula","Joan","Marc","ian","Sergi","Sebas","Jose Luis","oscar"]
os.mkdir("/home/joan/AO/Tasca10/UD11/Prova")
os.chdir("/home/joan/AO/Tasca10/UD11/Prova")
with open("ex12.txt","w") as f:
    print("Fitxer creat correctament!")
    for e in companys:
        f.write(e+"\n")
professors=["David","Pep","Fela","Lluis","Joan"]
with open ("ex12.txt","a+") as f:
    for e in professors:
        f.write(e+"\n")
a = []
with open("ex12.txt","r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)