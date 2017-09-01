with open('../data/rosalind_gc.txt', 'r') as f:
	data = ''.join(filter(lambda x:x, map(lambda x:x.strip(),f.readlines())))

data = data.split('>')[1:]
data = ((x[:13], x[13:]) for x in data)

res = {key:(value.count('G') + value.count('C'))/len(value)*100 for key,value in data}

res, name = max((v,k) for k,v in res.items())

print(name)
print(round(res, 6))