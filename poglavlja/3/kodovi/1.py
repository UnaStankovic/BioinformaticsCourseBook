from collections import deque
import copy

# Secenje DNK niske na k-mere
def string_to_k_mers(dna_string, k):
	k_mers = []

	for i in range(len(dna_string) - (k-1)):
		k_mer = dna_string[i:i+k]
		k_mers.append(k_mer)

	return k_mers

# Konstruisanje Debruijn grafa od k-mera
def debruijn_graph_from_k_mers(k_mers):
	G = {}

	for k_mer in k_mers:
		u = k_mer[:-1]
		v = k_mer[1:]

		if u in G:
			if v not in G[u]:
				G[u].append(v)
		else:
			G[u] = [v]

		if v not in G:
			G[v] = []

	return G


# Izracunavanje ulaznog i izlaznog stepena za zadati cvor
def degree(G, v):
	out_deg = len(G[v])
	in_deg = 0

	for u in G:
		if v in G[u]:
			in_deg += 1

	return (in_deg, out_deg)

# Pronalazenje izolovanih 1 in 1 out ciklusa u grafu polazeci od zadatog cvora
def isolated_cycle(G, v):
	cycle = []

	(in_deg, out_deg) = degree(G, v)

	while in_deg == 1 and out_deg == 1:
		u = G[v][0]
		cycle.append((v,u))
		if cycle[0][0] == cycle[-1][1]:
			return cycle

		v = u
		(in_deg, out_deg) = degree(G, v)

	return None


# Pronalazenje maksimalnih nerazgranatih putanja u grafu
def maximal_non_branching_paths(G):
	paths = []
	visited = {}

	for v in G:

		(v_in_deg, v_out_deg) = degree(G, v)
		if v_in_deg != 1 or v_out_deg != 1:
			
			visited[v] = True

			if v_out_deg > 0:
			
				for w in G[v]:
					non_branching_path = [(v,w)]

					visited[w] = True
					(w_in_deg, w_out_deg) = degree(G, w)
					
					while w_in_deg == 1 and w_out_deg == 1:
						u = G[w][0]
						non_branching_path.append((w,u))
						w = u
						visited[w] = True
						(w_in_deg, w_out_deg) = degree(G, w)

					paths.append(non_branching_path)
	
	for v in G:
		if v not in visited:
			c = isolated_cycle(G, v)
			if c != None:
				paths.append(c)

	return paths


# Konstruisanje DNK niske od dobijene putanje
def create_string_from_path(path):

	dna_string = path[0][0]

	for i in range(len(path)):
		dna_string += path[i][1][-1]

	return dna_string


def main():
	dna_string = "AATCGTGACCTCAACT"
	#               TCGTGAC
	#             AATC
	#                          ACT
	#                    ACCT
	#                         AAC
	#                       TCAAC
	k = 3                   
	k_mers = string_to_k_mers(dna_string, k)
	g = debruijn_graph_from_k_mers(k_mers)
	paths = maximal_non_branching_paths(g)
	
	print(paths)

if __name__ == "__main__":
	main()
