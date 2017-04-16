def count_string(sir = """The Heart of a Woman (1981) is the fourth of seven autobiographies by American writer Maya Angelou (pictured). She recounts events in her life between 1957 and 1962, as she travels to California, New York, Cairo and Ghana, and raises her teenage son. She becomes a published author active in the US civil rights movement, and is romantically involved with a South African freedom fighter. The book explores Angelou's theme of motherhood, and ends as she looks forward to newfound independence and freedom when her son leaves for college."""):
	dictionar = dict()
	rez = list()
	sir_split = sir.replace(',','').lower().split()
	dictionar = dictionar.fromkeys(sir_split,0)
	for substring in sir_split:
		dictionar[substring] = dictionar[substring]+1
	rez = dictionar.items()
	return rez
	