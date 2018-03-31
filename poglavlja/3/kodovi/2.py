from collections import deque
import copy

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

# Konstruisanje DNK niske od dobijene putanje
def create_string_from_path(path):

	dna_string = path[0][0].replace("'",'')

	for i in range(len(path)):
		dna_string += path[i][1].replace("'",'')[-1]

	return dna_string


# Pronalazenje cvorova od kojih postoje grane ka zadatom cvoru v
def incoming(G, v):
	in_list = []

	for u in G:
		if v in G[u]:
			in_list.append(u)

	return in_list

# Pronalazenje cvorova do kojih postoje grane od zadatog cvora v
def outgoing(G, v):
	return G[v]


# Pravljenje (u,v,w) "zaobilaznice" u zadatom grafu G
def bypass(G, u, v, w):
	G_p = copy.deepcopy(G)
	G_p[u].remove(v)
	G_p[v].remove(w)
	G_p[u].append(v+"'")  #v'
	G_p[v+"'"] = [w]
	return G_p


def DFS(G, v, visited):
	visited[v] = True

	for w in G[v]:
		if w not in visited:
			DFS(G, w, visited)


# Provera da li je graf povezan u odnosu na DFS obilazak iz zadatog cvora
def is_connected(G):

	visited = {};
	for v in G:
		DFS(G,v,visited)
		break;

	for v in G:
		if v not in visited:
			return False

	return True

# Pronalazenje svih Ojlerovih ciklusa u zadatom grafu G
def all_eulerian_cycles(G):
	all_graphs = deque([copy.deepcopy(G)])
	cycles = []

	while len(all_graphs) > 0:
		G_p = all_graphs.popleft()
		v_p = None
		for v in G_p:
			(in_deg, out_deg) = degree(G_p, v)

			if in_deg > 1:
				v_p = v
				break

		if v_p != None:
			for u in incoming(G_p, v_p):
				for w in outgoing(G_p, v_p):
					new_graph = bypass(G_p, u, v, w)
					if is_connected(new_graph):
						all_graphs.append(copy.deepcopy(new_graph))
		else:
			for k in G_p:
				cycle = isolated_cycle(G_p, k)
				if cycle != None:
					path = create_string_from_path(cycle)
					if path not in cycles:
						cycles.append(path);
	
	return cycles

	


def main():
	G = {'AT' : ['TC'], 'TC' : ['CG'], 'CG': ['GA','GG'], 'GA':['AT','AC'], 'AC':['CG'], 'GG':['GA']} 

	print(all_eulerian_cycles(G))

if __name__ == "__main__":
	main()
