with open('../data/rosalind_fib.txt') as f:
	n, k = map(int, f.read().strip().split())
print(n,k, '\n')
a, b = 1, 1
for _ in range(n-2):
	c, a = b + 3*a, b
	b = c
print(c)