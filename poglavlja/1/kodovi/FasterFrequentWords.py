def symbol_to_number(c):
    pairs = {
        'A' : 0,
        'T' : 1,
        'C' : 2,
        'G' : 3
    }
    return pairs[c]
        
def number_to_symbol(n):
    pairs = {
        0 : 'A',
        1 : 'T',
        2 : 'C',
        3 : 'G'
    }
    
    return pairs[n]

def number_to_pattern(n, k):
    if k == 1:
        return number_to_symbol(n)
    
    prefix_index = n // 4
    r = n % 4
    c = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    
    return prefix_pattern + c

def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    
    last = pattern[-1:]
    prefix = pattern[:-1]
    
    return 4 * pattern_to_number(prefix) + symbol_to_number(last)
    

def computing_frequencies(text, k):
    frequency_array = [0 for i in range(4**k)]
    
    for i in range(len(text) - k):
        pattern = text[i:i+k]
        j = pattern_to_number(pattern)
        frequency_array[j] += 1
    
    return frequency_array
        
def approx_pattern_count(text, pattern, d):
	count = 0
	for i in range(0, len(text) - len(pattern)):
		pattern1 = text[i:len(pattern)]
		if(hamming_distance(pattern, pattern1) <= d):
			count += 1
	return count 		

def hamming_distance(pattern, pattern1):
	count = 0
	for i in range(len(pattern) - 1):
		if(pattern[i] != pattern1[i]):
			count += 1
	return count

def neighbours(pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A','C','G','T']
	neighbourhood = set([])
	suffix_neighbours = neighbours(suffix(pattern), d)
	for text in suffix_neighbours:
		if hamming_distance(suffix(pattern), text) < d:
			for x in ['A','C','G','T']:
				neighbourhood.add(x)
			else:
				neighbourhood.add(first_symbol(pattern))
	return neighbourhood
		
def first_symbol(pattern):
	return pattern[0]

def suffix(pattern):
	return pattern[1:]	

def faster_frequent_words(text, k, d):
	frequent_patterns = set([])
	close = [0 for i in range(4**k - 1)]
	frequency_array = [0 for i in range(4**k - 1)]
	for i in range(len(text) - k):
		neighbourhood = neighbours(text[i:k], d)	
		for pattern in neighbourhood:
			index = pattern_to_number(pattern)
			close[index] = 1
	for i in range(0, 4**k - 1):
		if(close[i] == 1):
			pattern = number_to_pattern(i, k)
			frequency_array[i] =  approx_pattern_count(text, pattern, d)
	max_count = max(frequency_array)
	for i in range(0, 4**k - 1):
		if(frequency_array[i] == max_count):
			pattern = number_to_pattern(i,k)
			frequent_patterns.add(pattern)
	return frequent_patterns		
	
def main():
    print(faster_frequent_words('ATGCTGCTAGCTGACTATCGCATGCTAGCTAGCTAGCTAGCAT', 3, 1))
    
if __name__ == "__main__":
    main()
