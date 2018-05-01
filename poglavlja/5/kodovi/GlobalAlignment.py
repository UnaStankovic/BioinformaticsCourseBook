GAP_PENALTY = -2
MISSMATCH = 0
MATCH = 1

def match_score(c1, c2):
	if c1 == c2:
		return MATCH
	else:
		return MISSMATCH

def global_alignment(v, w):
	n = len(v)
	m = len(w)

	backtrack = [[(-1, -1) for j in range(m + 1)] for i in range(n + 1)]
	s = [[0 for j in range(m + 1)] for i in range(n + 1)]

	for i in range(1, n + 1):
		s[i][0] = s[i-1][0] + GAP_PENALTY
		backtrack[i][0] = (i-1, 0)

	for j in range(1, m + 1):
		s[0][j] = s[0][j-1] + GAP_PENALTY
		backtrack[0][j] = (0, j-1)

	for i in range(1, n + 1):
		for j in range(1, m + 1):
			s[i][j] = max(
							s[i-1][j] + GAP_PENALTY,
							s[i][j-1] + GAP_PENALTY,
							s[i-1][j-1] + match_score(v[i-1], w[j-1])
						 )

			if s[i][j] == s[i-1][j] + GAP_PENALTY:
				backtrack[i][j] = (i-1, j)

			elif s[i][j] == s[i][j-1] + GAP_PENALTY:
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
	w = "GGGCCCTT"

	print(global_alignment(v, w))

if __name__ == "__main__":
	main()
