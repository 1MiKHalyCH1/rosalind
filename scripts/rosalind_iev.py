with open('../data/rosalind_iev.txt') as f:
	data = map(int, f.read().strip().split())
multipliers = [1,1,1,.75,.5,0]

print(2*sum(k*v for k,v in zip(data,multipliers)))