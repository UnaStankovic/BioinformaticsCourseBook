#Formiranje sufiksnog niza na osnovu niza niski strings
def suffix_array_construction(strings):
	suffix_array = []

	for s in range(len(strings)):
		string = strings[s] + '$'
		for i in range(len(string)):
			suffix_array.append((string[i:],s, i))

	suffix_array.sort()
	return suffix_array

#Funkcija vraca pozicije na kojima se niska pattern pojavljuje u svakoj pojedinacnoj niski, u "okolini" pozicije mid
def find_neighborhood(suffix_array, mid, pattern):
	up = mid
	down = mid

	while up >= 0 and len(suffix_array[up][0]) > len(pattern) and suffix_array[up][0][:len(pattern)] == pattern:

		up -= 1

	while down < len(suffix_array) and len(suffix_array[down][0]) > len(pattern) and suffix_array[down][0][:len(pattern)] == pattern:
		
		down += 1

	positions = []

	for i in range(up+1, down):
		positions.append((suffix_array[i][1], suffix_array[i][2]))
	

	positions.sort()
	print(positions)
	return positions

#Trazenje pozicija na kojima se pojavljuje niska pattern u svakoj pojedinacnoj niski koja je ucestvovala u formiranju suffix_array-a
def pattern_matching_with_suffix_array(suffix_array, pattern):
	top = 0
	bottom = len(suffix_array)-1

	while top <= bottom:
		mid = (top + bottom) // 2

		if len(suffix_array[mid][0]) > len(pattern):
			if suffix_array[mid][0][:len(pattern)] == pattern:
				return find_neighborhood(suffix_array, mid, pattern)	

		if pattern < suffix_array[mid][0]:
			bottom = mid - 1
		else:
			top = mid + 1


def main():
	strings = ['ananas', 'and', 'antenna', 'banana', 'bandana', 'nab', 'nana', 'pan']

	suffix_array = suffix_array_construction(strings)

	pattern = 'an'

	print(pattern_matching_with_suffix_array(suffix_array, pattern))

if __name__ == "__main__":
	main()
