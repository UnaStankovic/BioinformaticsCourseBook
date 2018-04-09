import copy

# Formiranje ciklicnog spektra peptida
def cyclic_spectrum(peptide, amino_acid, amino_acid_mass):
	prefix_mass = [0]
	current_mass = 0
	for i in range(len(peptide)):
		for j in range(20):
			if amino_acid[j] == peptide[i]:
				prefix_mass.append(current_mass + amino_acid_mass[j])
				current_mass += amino_acid_mass[j]
				
	peptide_mass = prefix_mass[-1]
	cyclic_spectrum = [0]
	for i in range(len(prefix_mass)):
		for j in range(i+1, len(prefix_mass)):
			cyclic_spectrum.append(prefix_mass[j] - prefix_mass[i])
			if i > 0 and j < len(prefix_mass)-1:
				cyclic_spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
			
	cyclic_spectrum.sort()
	return cyclic_spectrum

# Prosirivanje liste peptida dodavanjem svih mogucih amino kiselina na kraj lanca
def expand(peptides, amino_acid):
	extension = []
	
	for peptide in peptides:
		for aa in amino_acid:
			extension.append(peptide + aa)
		
	return extension

# Izracunavanje ukupne mase peptida kao sume svih aminokiselina u lancu
def mass(peptide, amino_acid, amino_acid_mass):
	total_mass = 0
	
	for i in range(len(peptide)):
		for j in range(len(amino_acid)):
			if peptide[i] == amino_acid[j]:
				total_mass += amino_acid_mass[j]
				
	return total_mass

# Izdvajanje sume celog peptida iz spektra
def parent_mass(spectrum):
	return spectrum[-1]

# Formiranje linearnog spektra
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


# Provera da li je dati peptid konzistentan sa zadatim spektrom
def consistent(peptide, target_spectrum, amino_acid, amino_acid_mass):
	peptide_linear_spectrum = linear_spectrum(peptide, amino_acid, amino_acid_mass)
	
	for aa in peptide_linear_spectrum:
		found = False
		for aa_p in target_spectrum:
			if aa_p == aa:
				found = True
		if found == False:
			return False
			
	return True


# Sekvenciranje ciklopeptida
def cyclopeptide_sequencing(spectrum, amino_acid, amino_acid_mass):
	peptides = ['']
	i = 1;
	while len(peptides) > 0:
		next_peptides = []
		peptides = expand(peptides, amino_acid)
		next_peptides = copy.copy(peptides)
		for peptide in peptides:
			if mass(peptide, amino_acid, amino_acid_mass) == parent_mass(spectrum):
				if cyclic_spectrum(peptide, amino_acid, amino_acid_mass) == spectrum:
					print(peptide)
				next_peptides.remove(peptide)
			elif not consistent(peptide, spectrum, amino_acid, amino_acid_mass):
				next_peptides.remove(peptide)
		peptides = next_peptides
		
				
def main():
	amino_acid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
	amino_acid_mass = [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]
	
	peptide = "SPQR"
	
	spectrum = cyclic_spectrum(peptide, amino_acid, amino_acid_mass)
	
	cyclopeptide_sequencing(spectrum, amino_acid, amino_acid_mass)
	
if __name__ == "__main__":
	main()