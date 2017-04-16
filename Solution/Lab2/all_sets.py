def all_sets(lista = [1,2,3], partial_sol = set()):
	#print(lista)
	if lista == list():
		return [partial_sol]
	else:
		rez = list()
		rez.extend(all_sets(lista[1:],partial_sol))
		partial_sol = partial_sol.union({lista[0]})
		rez.extend(all_sets(lista[1:],partial_sol))
		return rez