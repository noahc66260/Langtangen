def L2(x, epsilon=1.0E-6):
	'''
	A more efficient implementation of the L2 function
	'''
	term = (x/(1.0+x))
	i = 1
	s = term
	while abs(term) > epsilon:
		a = (i/(i+1.0))*(x/(1.0+x))
		term = a*term
		i += 1
		s += term
	return s, i

def originalL2(x, epsilon=1.0E-6):
	x = float(x)
	i = 1
	term = (1.0/i)*(x/(1+x))**i
	s = term
	while abs(term) > epsilon: # abs(x) is |x|
		i += 1
		term = (1.0/i)*(x/(1+x))**i
		s += term
	return s,i

from math import log
x = 10
print 'Using originalL2...'
for k in range(4,14,2):
	epsilon = 10**(-k)
	approx, n = originalL2(x, epsilon=epsilon)
	exact = log(1+x)
	exact_error = exact - approx
	print 'epsilon: %5.0e, exact error: %8.2e, n=%d' % \
			(epsilon, exact_error, n)
print ""

print 'Using L2...'
for k in range(4,14,2):
	epsilon = 10**(-k)
	approx, n = L2(x, epsilon=epsilon)
	exact = log(1+x)
	exact_error = exact - approx
	print 'epsilon: %5.0e, exact error: %8.2e, n=%d' % \
			(epsilon, exact_error, n)
