def suffix_array_construction(string):
	suffix_array = []
	string += '$'
	for i in range(len(string)):
		suffix_array.append(string[i:])

	suffix_array.sort()
	return suffix_array


def find_neighborhood(suffix_array, mid, pattern):
	up = mid
	down = mid

	while up >=0 and len(suffix_array[up]) > len(pattern) and suffix_array[up][:len(pattern)] == pattern:
		up -= 1

	while down < len(suffix_array) and len(suffix_array[down]) > len(pattern) and suffix_array[down][:len(pattern)] == pattern:
		down += 1

	positions = []

	for i in range(up+1, down):
		positions.append(len(suffix_array) - len(suffix_array[i]))
	

	positions.sort()
	#print('hello')
	return positions


def pattern_matching_with_suffix_array(suffix_array, pattern):
	top = 0
	bottom = len(suffix_array) - 1

	

	while top <= bottom:
		mid = (top + bottom)//2

		if len(suffix_array[mid]) > len(pattern):
			if suffix_array[mid][:len(pattern)] == pattern:
				return find_neighborhood(suffix_array, mid, pattern)
		if pattern < suffix_array[mid]:
			bottom = mid - 1
		else:
			top = mid + 1

	 

def main():
	string = 'ananas'
	
	suffix_array = suffix_array_construction(string)

	pattern = 'an'

	print(pattern_matching_with_suffix_array(suffix_array, pattern))



if __name__ == '__main__':
	main()
