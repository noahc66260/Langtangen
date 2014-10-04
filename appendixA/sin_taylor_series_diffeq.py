from scitools.std import *

def S(x,n):
	'''
	Returns sum of first n+1 terms in Taylor series
	for sin(x) and the first neglected term
	'''
	ajm1 = x
	s = ajm1
	for j in range(1,n+1):
		aj = -x**2 / float((2*j+1)*(2*j)) * ajm1
		s += aj
		ajm1 = aj
	aj = -x**2 / float((2*j+1)*(2*j)) * ajm1 # first neglected term
	return s, aj

def _test():
	x = array(range(-5,5))
	actual = sin(x)
	n = 50
	approximation = [S(i,n)[0] for i in x]
	print 'Approximation for sin(x) using %d terms' % n
	print '%10s %15s %15s' % ('x', 'actual value', 'approximation')
	for i in range(len(approximation)):
		print '%10f %15f %15f' % (x[i], actual[i], approximation[i])

if __name__ == '__main__':
	_test()

'''
Approximation for sin(x) using 50 terms
         x    actual value   approximation
 -5.000000        0.958924        0.958924
 -4.000000        0.756802        0.756802
 -3.000000       -0.141120       -0.141120
 -2.000000       -0.909297       -0.909297
 -1.000000       -0.841471       -0.841471
  0.000000        0.000000        0.000000
  1.000000        0.841471        0.841471
  2.000000        0.909297        0.909297
  3.000000        0.141120        0.141120
  4.000000       -0.756802       -0.756802
'''
