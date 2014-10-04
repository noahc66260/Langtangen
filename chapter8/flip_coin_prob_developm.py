from scitools.std import *

N = 10**4
r = random.uniform(0,1,N)
h = where(r <= 0.5, 1, 0)
p = zeros(N)
for i in range(N):
	p[i] = sum(h[:i+1])/float(i+1)

q = cumsum(h)
I = arange(1,N+1)

print 'float_eq(p, q/I) = ', float_eq(p, q/I.astype(float))

plot(I,p,
	title='Number of flips vs. P(heads)', 
	xlabel='Number of flips', 
	ylabel='P(heads')
raw_input('Press Enter to quit: ')
