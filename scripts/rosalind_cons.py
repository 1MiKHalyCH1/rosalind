from collections import defaultdict

matrix = defaultdict(list)

with open('../data/rosalind_cons.txt') as f:
	data = ((x[:13], x[13:]) for x in ''.join(x.strip() for x in f.readlines()).split('>')[1:])

for e in zip(*list(zip(*data))[1]):
	for x in 'ACGT':
		matrix[x].append(e.count(x))

print(''.join(max((v[i], k) for k, v in matrix.items())[1] for i in range(len(matrix['A']))))

for x in 'ACGT':
	print(x+':',' '.join(map(str, matrix[x])))