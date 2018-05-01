def LCSBacktrack(v, w):
	n = len(v)
	m = len(w)
	s = [[0 for j in range(m + 1)] for i in range(n + 1)]

	backtrack = [[(-1,-1) for j in range(m + 1)] for i in range(n + 1)]

	for i in range(1, n + 1):
		backtrack[i][0] = (i-1, 0)

	for j in range(1, m + 1):
		backtrack[0][j] = (0, j-1)

	for i in range(1, n + 1):
		for j in range(1, m + 1):

			s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + int(v[i-1] == w[j-1]))

			if s[i][j] == s[i-1][j]:
				backtrack[i][j] = (i-1, j)
			elif s[i][j] == s[i][j-1]:
				backtrack[i][j] = (i, j-1)
			else:
				backtrack[i][j] = (i-1, j-1)

	i = backtrack[n][m][0]
	j = backtrack[n][m][1]

	lcs = ""

	if i == n-1 and j == m - 1:
		lcs = v[n-1]

	while not (i == 0 and j == 0):
		if backtrack[i][j] == (i-1, j-1):
			lcs = v[i-1] + lcs

		i = backtrack[i][j][0]
		j = backtrack[i][j][1]

	print(lcs)

	return s[n][m]

def main():
	v = "abcd"
	w = "dabe"

	print(LCSBacktrack(v,w))

if __name__ == "__main__":
	main()
