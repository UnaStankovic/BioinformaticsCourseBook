def number_to_symbol(n):
    pairs = {
            0: 'A',
            1: 'T',
            2: 'C',
            3: 'G'
        }
    
    return pairs[n]


def number_to_pattern(n, k):
    if k == 1:
        return number_to_symbol(n)
    
    prefix_index = n // 4
    r = n - n // 4
    symbol = number_to_symbol(r)
    
    return number_to_pattern(prefix_index, k - 1) + symbol


def hamming_distance(pattern_p, pattern):
    k = len(pattern_p)
    
    distance = 0
    
    for i in range(k):
        if pattern_p[i] != pattern[i]:
            distance += 1

    return distance


# Sumiranje hamingovih rastojanja izmednju pattern niske i svih DNK sekvenci 
def d(pattern, dna):
    k = len(pattern)
    distance = 0
    
    for dna_string in dna:
        
        h_dist = float('inf')
        
        for i in range(len(dna_string) - k):
            
            pattern_p = dna_string[i:i+k]
            dist = hamming_distance(pattern_p, pattern)
            
            if dist < h_dist:
                h_dist = dist
                
        distance += h_dist
    return distance

# Pronalazenje median niske
def median_string(dna, k):
    distance = float('inf')
    median = ''
    
# Za svaku od 4^k niski pretpostavimo da je median niska i proverimo kolika
# je njena udaljenost od DNK sekvenci
    for i in range(4**k):
        pattern = number_to_pattern(i, k)
        
        current_distance = d(pattern, dna)
        
	# Ako je tekuca kandidat median niska bolja od dosadasnje najbolje
	# vrednosti se azuriraju i pamti se najbolja
        if distance > current_distance:
            distance = current_distance
            median = pattern
            
    return median
    

def main():
    dna = [
            'GTAGATGTCATTAGCATGCAC',
            'CCTAGCCACTCTGCCATGTCG',
            'AACTCGTGCATTCTACGACTG',
            'AAACTTTCCGGATCTTCATAC',
            'CTACATCATCGAAGGCTACGC'
        ]
    
    print(median_string(dna, 4))
    

if __name__ == "__main__":
    main()
