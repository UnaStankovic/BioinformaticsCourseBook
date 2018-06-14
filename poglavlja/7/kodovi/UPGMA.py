class Cluster:
	def __init__(self, elements, age):
		self.elements = elements
		self.age = age
		self.left = None
		self.right = None

	def __str__(self):
		return ("s : d"  (self.elements, self.age))

	def add_left(self, L):
		self.left = L

	def add_right(self, R):
		self.right = R

def distance(D, cluster_1, cluster_2):
	d = 0
	n1 = len(cluster_1.elements)
	n2 = len(cluster_2.elements)

	for i in cluster_1.elements:
		for j in cluster_2.elements:
			d += D[i][j]

	return d/(n1*n2)

def min_distance(clusters, D, num_clusters):

	minimum = float('inf')
	min_i = -1
	min_j = -1

	for i in range(num_clusters):
		for j in range(i+1, num_clusters):
			dist = distance(D, clusters[i], clusters[j])
			if dist < minimum:
				minimum = dist
				min_i = i
				min_j = j

	return (min_i, min_j, minimum)


def UPGMA(D, n):
	clusters = [Cluster([i], 0) for i in range(n)]

	num_clusters = len(D)

	while num_clusters > 1:
		(i, j, distance) = min_distance(clusters, D, num_clusters)
		
		new_cluster = Cluster(clusters[i].elements + clusters[j].elements, distance/2)
		new_cluster.add_left(clusters[i])
		new_cluster.add_right(clusters[j])		

		new_clusters_list = []
		for c in range(num_clusters):
			if c != i and c != j:
				new_clusters_list.append(clusters[c])

		new_clusters_list.append(new_cluster)
		clusters = new_clusters_list[:]
		num_clusters -= 1
	
	return clusters[0]
		

		

def main():
	D = [
		[0,  13, 21, 22],
		[13,  0, 12, 13],
		[21, 12,  0, 13],
		[22, 13, 13,  0]
	]

	n = len(D)

	print(UPGMA(D, n))

if __name__ == "__main__":
	main()
