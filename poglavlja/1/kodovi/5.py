# Prevodjenje nukleotida u brojeve
def symbol_to_number(c):
    pairs = {
        'a' : 0,
        't' : 1,
        'c' : 2,
        'g' : 3
    }
    
    return pairs[c]

# Prevodjenje nukleotida u brojeve        
def number_to_symbol(n):
    pairs = {
        0 : 'a',
        1 : 't',
        2 : 'c',
        3 : 'g'
    }
    
    return pairs[n]

# Prevodjenje broja u odgovarajucu nukleotidnu sekvencu
def number_to_pattern(n, k):
    if k == 1:
        return number_to_symbol(n)
    
    prefix_index = n // 4
    r = n % 4
    c = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    
    return prefix_pattern + c



# Prevodjenje nukleotidne sekvence u odgovarajuci broj
def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    
    last = pattern[-1:]
    prefix = pattern[:-1]
    
    return 4 * pattern_to_number(prefix) + symbol_to_number(last)



# Hamingova distanca, broj pozicija karaktera na kojima se tekstovi 1 i 2 razlikuju,
# podrazumeva se da je duzina obe niske jednaka
def hamming_distance(text1, text2):
    distance = 0
    
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distance += 1
            
    return distance



# Brojanje pojavljivanja podsekvenci u tekstu koje se od uzorka razlikuju na najvise d pozicija
def approximate_pattern_count(text, pattern, d):
    count = 0
    
    for i in range(len(text) - len(pattern)):
        pattern_p = text[i:i+len(pattern)]
        
        if hamming_distance(pattern, pattern_p) <= d:
            count += 1
            
    return count
    

# Pronalazenje svih niski susednih zadatom uzorku sa razlikama na najvise d pozicija
def neighbors(pattern, d):
    if d == 0: # Ako je dozvoljena greska jednaka nuli onda je samo uzorak svoj sused bez gresaka
        return set([pattern])
    
    # Izlaz iz rekurzije:
    if len(pattern) == 1: # Ako je duzina uzorka jednaka 1, a dozvoljena greska je veca od nule, onda je moguce iskoristiti bilo koji karakter
        return set(['a', 't', 'c', 'g'])
    
    neighborhood = set([])
    
    suffix_neighbors = neighbors(pattern[1:], d) # Pronalaze se svi susedi duzine n-1
    
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d: # Ako se sused razlikuje na manje od d pozicija od podniske uzorka bez prvog karaktera
            for x in ['a','t','c','g']:
                neighborhood.add(x + text) # Moguce je dodati bilo koji karakter na pocetak suseda i time dobiti najvise d razlika
        else: # U suprotnom, sused se vec razlikuje na d pozicija od uzorka pa je dozvoljeno samo dodavanje ispravnog karaktera kako se
            neighborhood.add(pattern[0] + text) # razlika ne bi povecala preko d
            
    return neighborhood



def frequent_words_with_mismatches(text, k, d):
    frequent_patterns = set([])
    
    close = [0 for i in range(4**k)] # Kandidati za proveru
    frequency_array = [0 for i in range(4**k)]
    
    # Za svaki uzorak duzine k u tekstu evidentiraju se kandidat susedi cija pojavljivanja treba uzeti u razmatranje (niske koje se razlikuju od uzorka na najvise d pozicija)
    for i in range(len(text) - k):
        neighborhood = neighbors(text[i:i+k], d) # Pronalaze se kandidati
        
        for pattern in neighborhood:
            index = pattern_to_number(pattern) # Svaka kandidat sekvenca se prevodi u svoj odgovarajuci indeks
            close[index] = 1 # i evidentira
            
    # Za svaku kandidat sekvencu (koja je do sada pronadjena u tekstu sa greskom d), broji se pojavljivanje njenih d-suseda
    for i in range(4**k):
        if close[i] == 1:
                pattern = number_to_pattern(i, k)
                frequency_array[i] = approximate_pattern_count(text, pattern, d)
    
    max_count = max(frequency_array)
    
    # Pronalaze se one sekvence duzine k cija su pojavljivanja najzastupljenija
    for i in range(4**k):
        if frequency_array[i] == max_count:
            pattern = number_to_pattern(i, k)
            frequent_patterns.add(pattern)
    
    return frequent_patterns
    
    
    
    
def main():
    print(frequent_words_with_mismatches('tgactatcatcgtagtatcgatgtgcacacacgtgcgcgcgcgcgccctgtacatgatc', 5, 2))
    
if __name__ == "__main__":
    main()
    
    
    
    
