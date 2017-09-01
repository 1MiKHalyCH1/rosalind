with open('../data/rosalind_rna.txt', 'r') as f:
	data = f.read()
print(data.replace('T','U'))