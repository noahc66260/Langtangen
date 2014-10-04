def findPrimes(N):
	'''
	Uses sieve of Eratosthenes to find all primes between 1 and N, inclusive
	'''
	a = [1]*(N+1)
	p = []
	for i in range(2,N+1):
		if a[i] == 1:
			p.append(i)
		j = 2*i
		while j <= N:
			a[j] = 0
			j += i
	return p

N = 100
p = findPrimes(N)
print 'Primes less than or equal to', N, 'are...'
for i in p:
	print i, 
