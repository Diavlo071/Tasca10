def evaluar_majuscules(s):
	nummajuscules = sum(c.isupper() for c in s)
	numnumeros	= sum(c.isdigit() for c in s)
	numcaractersespecials = len(s)-(nummajuscules+numnumeros)
	return nummajuscules, numnumeros, numcaractersespecials;
    
# Programa principal
a = input("Indicar paraula a revisar: ")
nMaj, nNum, NCE = evaluar_majuscules(a)
print("La paraula introduida: ", a, " te:\n",
	nMaj, " majuscules \n",
	NCE, " Numero de  Caracteres")

