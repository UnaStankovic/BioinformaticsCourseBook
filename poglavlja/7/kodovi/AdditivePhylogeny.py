def find_path(T, start, stop):
	path = [(start, 0)]
	visited = {}
	visited[start] = True

	while len(path) > 0:
		v = path[-1][0]
		
		if v == stop:
			return path

		found = False

		for (w,e) in T[v]:
			if w not in visited:
				path.append((w,e))
				visited[w] = True
				found = True
				break

		if not found:
			path.pop()
	
	return []

def find_insertion_point(path, distance):
	current_distance = 0
	previous_vertex = path[0][0]

	for i in range(1, len(path)):
		v = path[i][0]
		e = path[i][1]

		current_distance += e
		next_vertex = v
		
		
		if distance <= current_distance:
			return (previous_vertex, next_vertex, e, current_distance - distance)

		previous_vertex = v
				

def insert_vertex_on_path(T, start, stop, distance):
	path = find_path(T, start, stop)
	(v, w, e, e_dist) = find_insertion_point(path, distance)

	if e_dist == 0:
		return (T, w)

	T[v].remove((w, e))
	T[w].remove((v, e))

	new_v = str(v) + str(w) + str(e_dist)

	T[new_v] = []

	T[new_v].append((w, e_dist))
	T[w].append((new_v, e_dist))

	T[new_v].append((v, e - e_dist))
	T[v].append((new_v, e - e_dist))

	return (T, new_v)
	

def three_leaves(D, n):
	for i in range(n-1):
		for k in range(i, n-1):
			if D[i][k] == (D[i][n-1] + D[n-1][k]):
				return (i, n, k)


def limb(D, j):
	
	minimum = float('inf')

	for i in range(j):
		for k in range(i+1, j):
			dist = (D[i][j] + D[j][k] - D[i][k])/2
			if dist < minimum:
				minimum = dist
	
	return int(minimum)

def additive_phylogeny(D, n):
	if n == 2:
		return {
			0: [(1, D[0][1])],
			1: [(0, D[1][0])]
		}

	limb_length = limb(D, n-1)

	for j in range(n-1):
		D[j][n-1] = D[j][n-1] - limb_length
		D[n-1][j] = D[j][n-1]

	(i, n, k) = three_leaves(D, n)

	x = D[i][n-1]

	T = additive_phylogeny(D, n - 1)

	(T, v) = insert_vertex_on_path(T, i, k, x)

	T[v].append((n-1, limb_length))
	T[n-1] = [(v, limb_length)]

	return T	


def main():

	D = [
		[0,  13, 21, 22],
		[13,  0, 12, 13],
		[21, 12,  0, 13],
		[22, 13, 13,  0]
	]

	n = len(D)

	print(additive_phylogeny(D, n))

if __name__ == "__main__":
	main()
	
