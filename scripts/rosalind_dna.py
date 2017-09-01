with open('../data/rosalind_dna.txt', 'r') as f:
	data = f.read()
print(data.count('A'), data.count('C'), data.count('G'), data.count('T'))