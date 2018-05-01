def local_alignment(string_1, string_2):
	DP = [[0 for j in range(len(string_2) + 1)] for i in range(len(string_1) + 1)]

	for i in range(len(string_1) + 1):
		DP[i][0] = 0

	for j in range(len(string_2) + 1):
		DP[0][j] = 0

	for i in range(1, len(string_1) + 1):
		for j in range(1, len(string_2) + 1):
			DP[i][j] = max(0, DP[i-1][j] - 2, DP[i][j-1] - 2, DP[i-1][j-1] + int(string_1[i-1] == string_2[j-1]))

	
	maximum = 0

	for i in range(len(DP)):
		for j in range(len(DP[i])):
			if DP[i][j] > maximum:
				maximum = DP[i][j]

	return maximum



def main():
	string_1 = 'ACGTGCTCG'
	string_2 = 'AATGCTCT'

	print(local_alignment(string_1, string_2))

if __name__ == "__main__":
	main()
