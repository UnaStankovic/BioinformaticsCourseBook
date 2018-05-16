import copy

def symbol_to_number(n):
    pairs = {
            'A': 0,
            'T': 1,
            'C': 2,
            'G': 3
        }
    
    return pairs[n]
    
# Formiranje profil matrice za zadati skup motiva
def profile_from_motifs(motifs, k, t):
    profile = [[1 for i in range(k)] for x in range(4)]
    
    for j in range(k):
        for i in range(t):
            index = symbol_to_number(motifs[i][j])
            profile[index][j] += 1
            
    for j in range(k):
        for i in range(4):
            profile[i][j] /= (t+2)
            
    return profile
 

# Izracunavanje verovatnoce pojave pattern sekvence u odnosu na zadati profil
def probability(pattern, profile):
    prob = 1
    
    for j in range(len(pattern)):
        c = pattern[j]
        index = symbol_to_number(c)
        
        prob *= profile[index][j]
        
    return prob
 
# Pronalazenje najverovatnijeg podstringa duzine k iz zadate DNK sekvence
# koji je najverovatniji u odnosu na zadati profil
def most_probable_k_mer(dna_string, profile, k):
    
    best_k_mer = ''
    best_probability = -1
    
    for i in range(len(dna_string) - k):
        pattern = dna_string[i:i+k]
        pattern_prob = probability(pattern, profile)
        
        if pattern_prob > best_probability:
            best_probability = pattern_prob
            best_k_mer = pattern
            
    return best_k_mer
   
# Izracunavanje ukupnog skora za skup motiva
def score(motifs, k):
    t = len(motifs)
    
    total_score = 0
    
    for j in range(k):
        
        counts = [0, 0, 0, 0]
        
        for i in range(t):
            c = motifs[i][j]
            index = symbol_to_number(c)
            counts[index] += 1
            
        max_index = 0
        
        for i in range(1,4):
            if counts[i] > counts[max_index]:
                max_index = i
                
        total_score += t - counts[max_index]
        
    return total_score
        
    
# Pohlepno pronalazenje motiv niski
def greedy_motif_search(dna, k, t):

# Pretpostavimo da najbolji skup motiv sekvenci predstavljaju
# prefiksi duzine k svih niski
    best_motifs = [dna_string[0:k] for dna_string in dna]

# i izracunamo njihov ukupan skor
    best_score = score(best_motifs, k)
    
    first_string = dna[0]
    
    for i in range(len(first_string) - k):

    	motifs = []

	# Za svaku podnisku duzine k iz prve DNK sekvence kazemo da u tekucoj
	# iteraciji predstavlja prvi motiv

        motifs.append(first_string[i:i+k])
        
	# Iz svake od preostalih t-1 DNK sekvenci izdvajamo podstring duzine k
	# koji je najverovatniji u odnosu na profil dobijen od motiva dobijenih iz
	# prethodnih iteracija. Taj podstring dodajemo u skup motiva kako bi se
	# koristio u narednoj iteraciju za pronalazenje sledeceg motiva

        for j in range(1, t):
            profile = profile_from_motifs(motifs, k, j)
            motifs.append(most_probable_k_mer(dna[j], profile, k))
                        
	# Sa svaki izgenerisami skup motiva proveravamo da li daje bolji skor
	# u odnosu na do sada najbolji pronadjen
        current_score = score(motifs, k)
        
	# Ako je trenutni skup motiva bolji od dosadasnjeg azuriraju se vrednosti
        if current_score < best_score:
            best_motifs = copy.deepcopy(motifs)
            best_score = current_score
        
    return best_motifs

def main():
    dna = [
            'GTAGATGTCATTAGCATGCAC',
            'CCTAGCCACTCTGCCATGTCG',
            'AACTCGTGCATTCTACGACTG',
            'AAACTTTCCGGATCTTCATAC',
            'CTACATCATCGAAGGCTACGC'
        ]
    
    print(greedy_motif_search(dna, 4, len(dna)))
    

if __name__ == "__main__":
    main()
