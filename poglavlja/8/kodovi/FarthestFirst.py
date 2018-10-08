import math
import random

def farthest_point(data, centers):

	max_dist = 0
	max_point = None

	for point in data:
		avg_dist = 0

		if point not in centers:
			for center in centers:
				avg_dist += dist(point, center)

			avg_dist /= len(centers)
			if avg_dist > max_dist:
				max_dist = avg_dist
				max_point = point

	return max_point

def dist(p1, p2):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def farthest_first(data, k):
	centers = [random.choice(data)]

	k-1

	while k > 1:
		data_point = farthest_point(data, centers)
		centers.append(data_point)
		k -= 1

	return centers

def main():
	data = [(-1,3),(2,-3),(0,0),(3,4),(-1,2)]

	k = 2

	print(farthest_first(data, k))

if __name__ == "__main__":
	main()