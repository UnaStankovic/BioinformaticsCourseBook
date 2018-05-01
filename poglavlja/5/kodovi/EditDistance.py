def edit_distance(v, w):
	n = len(v)
	m = len(w)
	
	s = [[0 for j in range(m + 1)] for i in range(n + 1)]
	backtrack = [[(-1, -1) for j in range(m + 1)] for i in range(n + 1)]

	for i in range(1, n + 1):
		s[i][0] = i
		backtrack[i][0] = (i-1, 0)

	for j in range(1, m + 1):
		s[0][j] = j
		backtrack[0][j] = (0, j-1)

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			s[i][j] = min(s[i-1][j] + 1, s[i][j-1] + 1, s[i-1][j-1] + int(v[i-1] != w[j-1]))

			if s[i][j] == s[i-1][j] + 1:
				backtrack[i][j] = (i-1, j)

			elif s[i][j] == s[i][j-1] + 1:
				backtrack[i][j] = (i, j-1)
			else:
				backtrack[i][j] = (i-1, j-1)

	v_p = ""
	w_p = ""

	i = n
	j = m

	while (i,j) != (0,0):
		if backtrack[i][j] == (i-1, j-1):
			v_p = v[i-1] + v_p
			w_p = w[j-1] + w_p

		elif backtrack[i][j] == (i-1, j):
			v_p = v[i-1] + v_p
			w_p = '-' + w_p

		else:
			v_p = '-' + v_p
			w_p = w[j-1] + w_p

		(i,j) = backtrack[i][j]

	print(v_p)
	print(w_p)

	return s[n][m]

def main():
	v = "AAATTTGGGCCCGGGAAATTTCCC"
	w = "AAACCCTTTGGGCCCTTTAAACCC"

	print(edit_distance(v, w))

if __name__ == "__main__":
	main()