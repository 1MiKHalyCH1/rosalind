with open('../data/rosalind_grph.txt') as f:
	data = ((x[:13], x[13:]) for x in''.join(x.strip() for x in f.readlines()).split('>')[1:])
data = {k:(v[:3], v[-3:]) for k, v in data}

graph = {e:list(x for x in set(data) - {e} if data[e][1] == data[x][0]) for e in data}

for k, v in graph.items():
	for e in v:
		print(k,e)