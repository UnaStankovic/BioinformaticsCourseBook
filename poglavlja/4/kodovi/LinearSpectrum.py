
# Formiranje linearnog spektra zadatog peptida
def linear_spectrum(peptide, amino_acid, amino_acid_mass):
    prefix_mass = [0]
    current_mass = 0
    for i in range(len(peptide)):
        for j in range(20):
            if amino_acid[j] == peptide[i]:
                prefix_mass.append(current_mass + amino_acid_mass[j])
                current_mass += amino_acid_mass[j]
                
    linear_spectrum = [0]
    for i in range(len(prefix_mass)):
        for j in range(i+1, len(prefix_mass)):
            linear_spectrum.append(prefix_mass[j] - prefix_mass[i])
            
    linear_spectrum.sort()
    return linear_spectrum


def main():
    
    # Lista aminokiselina
    amino_acid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    
    # Lista masa odgovarajucih aminokiselina
    amino_acid_mass = [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]
    
    # Zadati peptid
    peptide = "NQEL"
    
    spectrum = linear_spectrum(peptide, amino_acid, amino_acid_mass)
    print(spectrum)
    
if __name__ == "__main__":
    main()