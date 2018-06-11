def match(s1, s2):
	if s1 == s2:
		return 1
	else:
		return -4

def affine_gap_alignment(string_1, string_2):
	upper = [[float('-inf') for j in range(len(string_2) + 1)] for i in range(len(string_1) + 1)]
	lower = [[float('-inf') for j in range(len(string_2) + 1)] for i in range(len(string_1) + 1)]
	middle = [[float('-inf') for j in range(len(string_2) + 1)] for i in range(len(string_1) + 1)]

	middle[0][0] = 0

	for i in range(1, len(string_1) + 1):
		for j in range(1, len(string_2) + 1):
			upper[i][j] = max(-10 -0.5 + middle[i][j-1], (-0.5 + upper[i][j-1]), (-10 -0.5 + lower[i][j-1]))
			lower[i][j] = max(-10 -0.5 + middle[i-1][j], (-10 -0.5 + upper[i-1][j]), (-0.5 + lower[i-1][j]))
			middle[i][j] = max(match(string_1[i-1], string_2[j-1]) + middle[i-1][j-1], upper[i][j], lower[i][j])

	return max(upper[len(string_1)][len(string_2)], middle[len(string_1)][len(string_2)], lower[len(string_1)][len(string_2)])

def main():

	string_1 = 'ACGTGCTCG'
	string_2 = 'AATGCTCT'
	
	print(affine_gap_alignment(string_1, string_2))

if __name__ == "__main__":
	main()