
def add_to_trie(Trie, pattern,  number_of_nodes, pattern_id):

	current_node = 'root'

	for c in pattern:

		if c in Trie[current_node]:
			current_node = Trie[current_node][c]
		else:
			if c != '$':
				Trie['i' + str(number_of_nodes)]={}
				Trie[current_node][c] = 'i' + str(number_of_nodes)
				current_node = 'i' + str(number_of_nodes)
				number_of_nodes += 1
			else:
				Trie[current_node][c] = pattern_id
				Trie['P' + str(pattern_id)]={}
				
	return (Trie, number_of_nodes)	

def trie_construction(patterns):
	Trie = {}
	Trie['root'] = {}

	number_of_nodes = 1

	for i in range(len(patterns)):
		pattern = patterns[i]
		(Trie,  number_of_nodes) = add_to_trie(Trie, pattern+'$' , number_of_nodes, i)

	return Trie

def prefix_trie_pattern_matching(text, Trie):
	v = 'root'
	for c in text:
		if c not in Trie[v]:
			return False
		
		v = Trie[v][c]

		if '$' in Trie[v]:
			return Trie[v]['$']

	return False


def trie_matching(text, Trie):
	found_patterns = []
	while len(text) > 0:
		res = prefix_trie_pattern_matching(text, Trie)
		if res != False:
			found_patterns.append(res)
		text = text[1:]
	return found_patterns

def main():

	patterns = ['ananas', 'and', 'antenna', 'banana', 'bandana', 'nab', 'nana', 'pan']

	query = 'bananananaspand'
	Trie = trie_construction(patterns)
	#print(prefix_trie_pattern_matching(query, Trie))
	print(trie_matching(query, Trie))
if __name__ == "__main__":
	main()



