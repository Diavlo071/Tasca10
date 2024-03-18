class Animal():
    def __init__(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        pass
    def mourem():
        pass
    def quisoc():
        print("Soc un animal")


class Cavall(Animal):
    def xerrar(self):
        print("Iiiiiiiiiii")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc un Cavall")
class Dofi(Animal):
    def xerrar(self):
        print("IchIchIchIch")
    def mourem(self):
        print("Em moc nadan")
    def quisoc(self):
        print("Soc un Dofi")
class Abella(Animal):
    def xerrar(self):
        print("Ssssssssss")
    def mourem(self):
        print("Em moc Volant")
    def quisoc(self):
        print("Soc una Abella")
    def  picar(self):
        print("Si me empreyes et picare")
class Huma(Animal):
    def __init__(self, atribut, edat, nom):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar():
        print("Hola soc un huma nosaltres parlem")
    def mourem(self):
        print("Em moc Caminant a un ritme de 4/2")
    def quisoc(self):
        print("Soc una Abella")
class Centaure(Huma,Cavall):
    def xerrar(self):
        print("Hola soc un huma nosaltres parlem")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Soc una Centaure")
class Fiet():
    def __init__(self, atribut, edat, nom, llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("*Insert crying child*")
    def mourem(self):
        print("Em moc gategant")
    def quisoc(self):
        print("Soc un Fiet")
    def nompares(self):
        for e in self.pares:
            print(e.nom)

class xou():
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Em moc fent xou")
    def quisoc(self):
        print("Soc un xou")

#Programa Principal
        
a = [Cavall("Marro","4"),Dofi("Gris","10"),Abella("Negra_i_groga","0,5"),Huma("Silbia","Cristia","7"),Centaure("Fiona","Marron","18"),Fiet("Jordi","Moreno","9",["Fiona","Marc"]),xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()