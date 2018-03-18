def pattern_to_number(pattern):
	if len(pattern) == 0:
		return 0
	last = pattern[-1]
	prefix = pattern[:-1]
	return 4 * pattern_to_number(prefix) + symbol_to_number(last)

def number_to_pattern(n, k):
	if k == 1:
		return number_to_symbol(n)
	prefixIndex = n // 4
	r = n $%$ 4
	symbol = number_to_symbol(r) 
	prefix  = number_to_pattern(prefixIndex, k-1)
	return prefix + symbol
	
def symbol_to_number(c):
	pairs = {
		'a' : 0,
		't' : 1,
		'c' : 2,
		'g' : 3
	} 
	return pairs[c]

def number_to_symbol(n):
	pairs = {
		0 : 'a',
		1 : 't',
		2 : 'c',
		3 : 'g'
	}
	return pairs[n]
	
def pattern_count(text, pattern):
    count = 0
    k = len(pattern)
    for i in range(len(text) - k):
        if text[i:i+k] == pattern:
            count += 1
    return count

def frequent_words(text, k, min_count):
    frequent_patterns = set([])
    count = []
    n = len(text)-k
    for i in range(n):
        pattern = text[i:i+k]
        count.append(pattern_count(text, pattern))
    max_count = max(count)
    if max_count < min_count:
        return []    
    for i in range(n):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    return frequent_patterns

def main():
	print(number_to_pattern(pattern_to_number('ta'),2))
	
if __name__ == "__main__":
    main()
