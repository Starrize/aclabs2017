def count_string(sir):
	rez = dict()
	sir_split = sir.replace(',','').lower().split()
	rez = rez.fromkeys(sir_split,0)
	for substring in sir_split:
		rez[substring] = rez[substring]+1
	return rez
	