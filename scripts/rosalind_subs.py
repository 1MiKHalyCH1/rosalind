import re

with open('../data/rosalind_subs.txt') as f:
	s, sub = map(lambda x:x.strip('\n'), f.readlines())

print(' '.join(map(str,(m.start()+1 for m in re.finditer('(?='+sub+')', s)))))