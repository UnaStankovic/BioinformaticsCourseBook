#Funkcija vraca indeks count-og pojavljivanja karaktera c u niski first_column, ukoliko se c pojavljuje bar count puta; inace ne vraca nista
def last_to_first(first_column, c, count):
	for i in range(len(first_column)):
		if first_column[i] == c:
			if count == 1:
				return i
			count -= 1

#Formiranje matrice svih ciklicnih rotacija niske s
def BWT(s):
	matrix = []
	s += '$'

	for i in range(len(s)):
		matrix.append(s)
		s = s[1:] + s[0]

	matrix.sort()
	return [row[-1] for row in matrix]

#Trazenje broja pojavljivanja niske pattern koriscenjem BWT algoritma
def bw_matching(first_column, last_column, pattern):
	top = 0
	bottom = len(last_column) - 1

	while top <= bottom:
		if len(pattern) > 0:
			symbol = pattern[-1]
			pattern = pattern[:-1]

			subset = last_column[top:bottom+1]
			
			if subset.index(symbol) != -1:
				top_index = -1
				bottom_index = -1

				for i in range(top, bottom+1):
					if symbol == last_column[i]:
						if top_index == -1:
							top_index = i
						bottom_index = i

				top_count = 0

				for i in range(top_index+1):
					if last_column[i] == symbol:
						top_count += 1

				bottom_count = top_count

				for i in range(top_index+1, bottom_index + 1):
					if last_column[i] == symbol:
						bottom_count += 1

				top = last_to_first(first_column, last_column[top_index], top_count)
				bottom = last_to_first(first_column, last_column[bottom_index], bottom_count)

			else:
				return 0

		else:
			return bottom - top + 1

def main():
	s = 'panamabananas'

	last_column = BWT(s)

	pattern = 'ana'

	first_column = last_column[:]
	first_column.sort()

	print(bw_matching(first_column, last_column, pattern))



if __name__ == "__main__":
	main()
