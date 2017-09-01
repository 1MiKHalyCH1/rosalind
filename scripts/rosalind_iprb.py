with open('../data/rosalind_iprb.txt') as f:
	k,m,n = map(int,f.read().strip().split())

print(k,m,n)
print((4*k*(k-1) + 3*m*(m-1) + 4*(2*k*m + 2*k*n + m*n))/(4 * (k+m+n) * (k+m+n-1)))