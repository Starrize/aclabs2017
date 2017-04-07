def flatten(lista, depth=1, sol=None):
	if depth == 0:
		return lista
	sol = []

	for item in lista:
		if isinstance(item,list):
			sol.extend(item)
		else:
			sol.append(item)
	return flatten(sol, depth-1)