# Sastavljanje DNK niske pomocu k-mera
def string_spelled_by_patterns(patterns, k):
	dna_string = patterns[0][:-1]

	for i in range(0, len(patterns)):
		dna_string += patterns[i][-1]

	return dna_string

# Sastavljanje DNK niske pomocu parova k-mera na udaljenosti d
def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
	first_patterns = [s[0] for s in gapped_patterns]
	second_patterns = [s[1] for s in gapped_patterns]

	prefix_string = string_spelled_by_patterns(first_patterns, k)
	suffix_string = string_spelled_by_patterns(second_patterns, k)

	print(prefix_string)
	print(suffix_string)

	for i in range(k+d, len(prefix_string)):
		if prefix_string[i] != suffix_string[i-k-d]:
			print('There is no string spelled by the gapped patterns')
			return ''
	return prefix_string + suffix_string[-k-d:]


def main():
	gapped_patterns = [('CTG','CTG'),('TGA','TGA'),('GAC','GAC'),('ACT','ACT')]

	print(string_spelled_by_gapped_patterns(gapped_patterns, 3, 1))

if __name__ == "__main__":
	main()


