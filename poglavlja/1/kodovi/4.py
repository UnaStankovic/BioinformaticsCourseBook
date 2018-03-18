#GC-skew
import matplotlib.pyplot as plt 

def draw_skew(skew):
	x = [i for i in range(len(skew))]
	ax = plt.subplot()
	ax.plot(x, skew)
	plt.show()

def calculate_skew(text):
	skew = [0 for c in text]
	last = 0
	for i in range(0, len(text)):
		if text[i] == 'g':
			skew[i] = last + 1
		elif text[i] == 'c':
			skew[i] = last - 1
		else:
			skew[i] = last
		last = skew[i]
	return skew


def main():
	text = "catgggcatcggccatacgcc"
	print(calculate_skew(text))
	draw_skew(calculate_skew(text))
	
if __name__ == "__main__":
    main()
