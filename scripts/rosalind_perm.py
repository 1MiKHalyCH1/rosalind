import itertools

with open('../data/rosalind_perm.txt') as f:
	n = int(f.read())

counter = 0
for e in itertools.permutations(range(1,n+1), n):
	counter += 1
	print(' '.join(map(str,e)))

print(counter)