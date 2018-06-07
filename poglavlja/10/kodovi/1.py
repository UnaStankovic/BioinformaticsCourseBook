def HMM(strings_pos, strings_neg):
	
	HMM = {}
	# HMM['0']['A+'] = 0.125
	# HMM['0']['T+'] = 0.125
	# HMM['0']['C+'] = 0.125
	# HMM['0']['G+'] = 0.125
	# HMM['0']['A-'] = 0.125
	# HMM['0']['T-'] = 0.125
	# HMM['0']['C-'] = 0.125
	# HMM['0']['G-'] = 0.125

	for string in strings_pos:
		for i in range(1, len(string)):
			c_prev_state = string[i-1] + '+'
			c_curr = string[i]

			if c_prev_state not in HMM:
				HMM[c_prev_state] = {}
				HMM[c_prev_state]['state'] = 1
				HMM[c_prev_state]['nucleotide'] = string[i-1]
				HMM[c_prev_state]['transitions'] = {}

			if c_curr not in HMM[c_prev_state]['transitions']:
				HMM[c_prev_state]['transitions'][c_curr] = 0

			HMM[c_prev_state]['transitions'][c_curr] += 1

	for string in strings_neg:
		for i in range(1, len(string)):
			c_prev_state = string[i-1] + '-'
			c_curr = string[i]

			if c_prev_state not in HMM:
				HMM[c_prev_state] = {}
				HMM[c_prev_state]['state'] = 0
				HMM[c_prev_state]['nucleotide'] = string[i-1]
				HMM[c_prev_state]['transitions'] = {}

			if c_curr not in HMM[c_prev_state]['transitions']:
				HMM[c_prev_state]['transitions'][c_curr] = 0

			HMM[c_prev_state]['transitions'][c_curr] += 1

	for source in HMM:
		output_sum = 0
		for dest in HMM[source]['transitions']:
			output_sum += HMM[source]['transitions'][dest]

		for dest in HMM[source]['transitions']:
			HMM[source]['transitions'][dest] = (HMM[source]['transitions'][dest] / output_sum) * 0.98

		HMM[source]['0'] = 0.02


	return HMM

def viterbi(HMM, string):
	i = 1

	matrix = [{} for i in range(len(string))]
	path = ""

	for i in range(len(string)):
		nucleotide = string[i]

		state_number = 0

		if i > 0:
			path += max_transition_state

		max_transition_prob = -1
		max_transition_state = ''

		for state in HMM:

			if HMM[state]['nucleotide'] != nucleotide:
				matrix[i][state] = 0

			elif i == 0:
				if HMM[state]['nucleotide'] == nucleotide:
					matrix[i][state] = 0.125

			else:
				max_prev = -1
				max_prev_state = ''

				for prev_state in matrix[i-1]:
					if HMM[prev_state]['state'] == HMM[state]['state']:
						state_change_prob = 0.99
					else:
						state_change_prob = 0.01

					if HMM[state]['nucleotide'] in HMM[prev_state]['transitions']:
						transition_prob = HMM[prev_state]['transitions'][HMM[state]['nucleotide']]
					else:
						transition_prob = 0

					curr_state = matrix[i-1][prev_state] * transition_prob * state_change_prob
					# print('{} -> {}'.format(prev_state, state))
					# print('{} = {} * {} * {}'.format(curr_state, matrix[i-1][prev_state], transition_prob, state_change_prob))

					if curr_state > max_prev:
						max_prev = curr_state
						max_prev_state = prev_state

				matrix[i][state] = max_prev

				if max_prev > max_transition_prob:
					max_transition_prob = max_prev
					max_transition_state = max_prev_state

		# print(matrix)
		# print('-------------------------')

	max_end = -1
	max_end_state = ''
	
	n = len(string)
	for state in matrix[n-1]:
		if matrix[n-1][state] > max_end:
			max_end = matrix[n-1][state]
			max_end_state = state

	path += max_end_state

	return path





def main():
	strings_pos = ['ACACAGACGCACA','CACATAGACAGGCATACACA', 'AAATACAGTATCTTTGCACTCCCGGAGTGCGG']
	strings_neg = ['CGAGCGTGTGAGTGAGAGATGAG', 'GTGGAACAGTAGGTAGGAGAGTG', 'AAATACAGTATCTTTGCACTCCCGGAGTGCGG']

	model = HMM(strings_pos, strings_neg)
	print(viterbi(model, 'CTCACGAGAGCCACAC'))

if __name__ == "__main__":
	main()
