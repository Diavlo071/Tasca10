dic = {'nom':'Joan','cognom':'Ramis','edat':30,'telefon': '971360133'}
for element in dic:
    print("La clau {} te el valor {}\n".format(element,dic[element]))
#Segona part
for x,y in dic.items():
    print("La clau {} i el seu valor es {}\n".format(x,y))
#dic .clear()
b = {'nom':'Pera', 'carrer': 'si'}
dic.update(b)
print(dic)