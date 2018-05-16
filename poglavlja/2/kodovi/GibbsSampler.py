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

# Pronalazenje skupa motiva nakon N iteracija koriscenjem Gibs sampler-a
def gibbs_sampler(dna, k, t, N):
    motifs = random_k_mers(dna, k, t)
    best_motifs = copy.deepcopy(motifs)
    best_score = score(best_motifs, k)
    
    for j in range(N):
        
        # Biramo slucajno i iz skupa [0,t)
        i = random.randrange(0,t)
        
        # Formiramo skup motiva koji se sastoji od svih dosadasnjih motiva osim i-tog
        selected_motifs = copy.deepcopy(motifs)
        del selected_motifs[i]
        
        # Pravimo profil od odabranih motiva (bez i-tog)
        profile = profile_from_motifs(selected_motifs, k, t-1)
        
        # Za i-ti motiv postavljamo najverovatniji podstring duzine k iz i-te DNK sekvence, u odnosu na dobijeni profil
        motifs[i] = most_probable_k_mer(dna[i], profile, k)
        del selected_motifs
        
        # Ako dobijeni motiv ima skor bolji od do sada najboljeg, vrednosti se azuriraju
        current_score = score(motifs, k)
        
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
    
    print(gibbs_sampler(dna, 4, len(dna), 500))
    

if __name__ == "__main__":
    main()
