import copy

def cycle_to_chromosome(nodes):
	
	chromosomes = [0 for i in range(len(nodes)//2)]

	for j in range(len(nodes)//2):
		if nodes[2*j] < nodes[2*j+1]:
			chromosomes[j] = nodes[2*j+1] // 2
		else:
			chromosomes[j] = -nodes[2*j] // 2
			
	return chromosomes
	
def colored_edges(P):
	edges = []
	for chromosome in P:
		nodes = chromosome_to_cycle(chromosome)
		for j in range(len(chromosome)):
			# Obojene grane su neusmerene, pa dodajemo oba smera
			edges.append((nodes[2*j+1], nodes[(2*j+2) % len(nodes)]))
			edges.append((nodes[(2*j+2) % len(nodes)],nodes[2*j+1]))
			
	return edges

def chromosome_to_cycle(chromosome):

	nodes = [0 for i in range(2*len(chromosome))]

	for j in range(len(chromosome)):
		i = chromosome[j]
		if i > 0: 
			nodes[2*j] = 2*i - 1
			nodes[2*j + 1] = 2*i
		else:
			nodes[2*j] = -2*i
			nodes[2*j + 1] = -2*i - 1
	return nodes
	
	
def graph_to_genome(genome_graph):
	P = []
	nodes = []
	
	for (i,j) in genome_graph:
		nodes.append(i)
		nodes.append(j)
	
	
	prvi = [nodes[-1]]
	ostatak = copy.copy(nodes[:-1])
	nodes = prvi + ostatak
	
	chromosome = cycle_to_chromosome(nodes)
	P.append(chromosome)
		
	return P	
	
def two_break_on_genome_graph(genome_graph, i, ip, j, jp):

	new_edges = []
	
	for edge in genome_graph:
		if (edge[0] == i and edge[1] == ip) or (edge[0] == j and edge[1] == jp):
			continue
		new_edges.append(edge)
		
	new_edges.append((i,j))
	new_edges.append((ip,jp))
	
	return new_edges
	
def black_edges(P):
	nodes = chromosome_to_cycle(P)
	edges = []
	i = 0;
	
	while i < len(nodes):
		if nodes[i] < nodes[i+1]:
			edges.append((nodes[i], nodes[i+1]))
		else:
			edges.append((nodes[i+1], nodes[i]))
			
		i = i + 2
		
	return edges
	
def two_break_on_genome(P, i, ip, j, jp):
	genome_graph = black_edges(P) + colored_edges([P])
	genome_graph = two_break_on_genome_graph(genome_graph, i, ip, j, jp)
	
	P = graph_to_genome(genome_graph)
	
	return P
	
def has_nontrivial_cycle(P, Q):
	for (v,w) in P:
		if (v,w) not in Q and (w,v) not in Q:
			return True

	return False

def select_edge_from_nontrivial_cycle(P, Q):
	for (v,w) in Q:
		if (v,w) not in P and (w,v) not in P:
			return (v,w)


def shortest_rearrangement_scenario(P, Q):
	red_edges = colored_edges([P])
	blue_edges = colored_edges([Q])
	
	num_of_breaks = 0

	while has_nontrivial_cycle(red_edges, blue_edges):	
		(j,i_p) = select_edge_from_nontrivial_cycle(red_edges, blue_edges)

		i = -1
		j_p = -1

		for (v,w) in red_edges:
		 	if v == j:
		 		i = w
		 	if w == j:
		 		i = v
		 	if v == i_p:
		 		j_p = w

		red_edges.remove((j, i))
		red_edges.remove((i, j))

		red_edges.remove((i_p, j_p))
		red_edges.remove((j_p, i_p))

		red_edges.append((j, i_p))
		red_edges.append((i_p, j))

		red_edges.append((j_p, i))
		red_edges.append((i, j_p))

		num_of_breaks += 1
	return num_of_breaks
	
def main():
	P = [1,-2,-3,4]
	Q = [1, 2, 3, -4]

	print(shortest_rearrangement_scenario(P,Q))
	
if __name__ == "__main__":
	main()

