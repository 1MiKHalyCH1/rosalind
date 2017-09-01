swap_dict = {
	'A':'T',
	'T':'A',
	'G':'C',
	'C':'G'
}

with open('../data/rosalind_revc.txt', 'r') as f:
	data = f.read().strip()
print(data)
print()
print(''.join(swap_dict[e] for e in data[::-1]))