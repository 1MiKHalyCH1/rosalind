with open('../data/rosalind_hamm.txt') as f:
	data = map(lambda x:x.strip('\n'), f.readlines())
print(sum(1 for x,y in zip(*data) if x!=y))