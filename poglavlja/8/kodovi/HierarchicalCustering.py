import math

T = {}

def find_closest(Dp, n):

	min_i = None
	min_j = None
	min_dist = float('inf')

	for i in Dp:
		for j in Dp[i]:
			if i != j:
				if Dp[i][j] < min_dist:
					min_dist = Dp[i][j]
					min_i = i
					min_j = j

	return (min_i, min_j)

def parse_matrix(D, n):
	
	Dp = {}	
	for i in range(len(D)):
		if i not in Dp:
			Dp[i] = {}
		for j in range(len(D[i])):
			if j not in Dp:
				Dp[j] = {}
			Dp[i][j] = D[i][j]
			Dp[j][i] = D[i][j]

	return Dp


def calculate_Dp(Dp, new_key, ci, cj):
	Dp[new_key] = {}
	for v in Dp:
			if v != ci and v != cj and v != new_key:
				if v in Dp:
					Dp[v][new_key] = (Dp[v][ci] + Dp[v][cj]) / 2
					Dp[new_key][v] = (Dp[v][ci] + Dp[v][cj]) / 2
	return Dp

def hierarchical_clustering(D, n):

	Dp = parse_matrix(D, n)

	clusters = []

	for i in range(n):
		clusters.append(i)
		T[i] = {'l':None, 'r':None, 'age':0}

	while n > 1:
		(ci, cj) = find_closest(Dp, n) 		

		new_key = str(ci)+str(cj)

		T[new_key] = {'l':ci, 'r':cj}
		clusters.remove(ci)
		clusters.remove(cj)

		Dp = calculate_Dp(Dp, new_key, ci, cj)

		del Dp[ci]
		del Dp[cj]
		
		for v in Dp:
			if v != new_key:
				del Dp[v][ci]
				del Dp[v][cj]

		clusters.append(new_key)

		n -= 1

	return T

def calculate_distances(points):
	D = [[0 for i in points] for j in points]

	for p1 in range(len(points)):
		for p2 in range(len(points)):
			D[p1][p2] = euclid_distance(points[p1], points[p2])
			
	return D

def euclid_distance(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def main():
	points = [(-1, 2), (2, 3), (1, 15), (2, -4)]
	D = calculate_distances(points)
	n = len(D)

	print(hierarchical_clustering(D, n))

if __name__ == "__main__":
	main()

		
