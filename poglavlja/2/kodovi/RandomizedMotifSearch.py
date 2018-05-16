import copy
import random

def symbol_to_number(n):
    pairs = {
            'A': 0,
            'T': 1,
            'C': 2,
            'G': 3
        }
    
    return pairs[n]

def probability(pattern, profile):
    prob = 1
    
    for j in range(len(pattern)):
        c = pattern[j]
        index = symbol_to_number(c)
        
        prob *= profile[index][j]
        
    return prob

# Izdvajanje pseudoslucajno odabranih podniski iz DNK sekvenci u skupu
def random_k_mers(dna, k, t):
    k_mers = []
    
    for i in range(t):
        start = random.randrange(0, len(dna[i]) - k)
        dna_string = dna[i]
        k_mers.append(dna_string[start:start+k])

    return k_mers


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
 
# Pronalazenje podniski DNK sekvenci iz skupa koje su najverovatnije u
# odnosu na zadati profil i one zajedno cine skup motiva
def motifs_from_profile(profile, dna):
    motifs = []
    k = len(profile[0])
    
    for dna_string in dna:
        motifs.append(most_probable_k_mer(dna_string, profile, k))

    return motifs


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

# Pronalazenje motiva koriscenjem algoritma za pseudoslucajni izbor
def randomized_motif_search(dna, k, t):

# Pretpostavimo da najbolji skup motiva cine slucajno odabrane podniske
# iz skupa DNK sekvenci
    motifs = random_k_mers(dna, k, t)
    best_motifs = copy.deepcopy(motifs)
    best_score = score(best_motifs, k)

# Dok se skor popravlja svakom iteracijom:   
    while True:

	# Formiramo profil od tekucih motiva
        profile = profile_from_motifs(motifs, k, t)

	# A zatim motive od dobijenog profila
        motifs = motifs_from_profile(profile, dna)
        
        current_score = score(motifs, k)
        
        if current_score < best_score:
            best_score = current_score
            best_motifs = copy.deepcopy(motifs)
        else:
            return best_motifs
        
        
def main():
    dna = [
            'GTAGATGTCATTAGCATGCAC',
            'CCTAGCCACTCTGCCATGTCG',
            'AACTCGTGCATTCTACGACTG',
            'AAACTTTCCGGATCTTCATAC',
            'CTACATCATCGAAGGCTACGC'
        ]
    
    print(randomized_motif_search(dna, 4, len(dna)))
    

if __name__ == "__main__":
    main()
