def invert (lista):
	nlist = []
	for x in lista:
		if lista[x] % 2 == 1:
			nlist.append(-1 * lista[x])
	return nlist
