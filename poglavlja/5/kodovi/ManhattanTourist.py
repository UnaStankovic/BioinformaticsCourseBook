def manhattan_tourist(n, m, down, right):
	s = [[0 for j in range(m)] for i in range(n)]

	backtrack = [[(0,0) for j in range(m)] for i in range(n)]

	backtrack[0][0] = (-1, -1)

	for i in range(1,n):
		s[i][0] = s[i-1][0] + down[i][0]
		backtrack[i][0] = (i-1, 0)

	for j in range(1,m):
		s[0][j] = s[0][j-1] + right[0][j]
		backtrack[0][j] = (0, j-1)

	for i in range(1, n):
		for j in range(1, m):

			to_down = s[i-1][j] + down[i][j]
			to_right = s[i][j-1] + right[i][j]

			if to_down > to_right:
				backtrack[i][j] = (i-1, j)
				s[i][j] = to_down
			else:
				backtrack[i][j] = (i, j-1)
				s[i][j] = to_right

	i = n-1
	j = m-1
	while backtrack[i][j] != (-1,-1):
		print(backtrack[i][j])
		i = backtrack[i][j][0]
		j = backtrack[i][j][1]

	return s[n-1][m-1]

def main():
	down = [[0, 0, 0, 0],
			[0, 1, 2, 1],
			[0, 1, 1, 1],
			[0, 1, 1, 1]]

	right = [[0, 0, 0, 1],
			 [0, 3, 5, 1],
			 [0, 1, 0, 1],
			 [0, 1, 0, 1]]

	print(manhattan_tourist(3, 3, down, right))

if __name__ == "__main__":
	main()