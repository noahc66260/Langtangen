from scitools.std import *

def S(x,n):
	'''
	Returns sum of first n+1 terms in Taylor series
	for cos(x) and the first neglected term
	'''
	ajm1 = 1
	s = ajm1
	for j in range(0,n):
		aj = -x**2 / float((2*j+1)*(2*j+2)) * ajm1
		s += aj
		ajm1 = aj
	aj = -x**2 / float((2*j+1)*(2*j+2)) * ajm1 # first neglected term
	return s, aj

def _test():
	x = array(range(-5,5))
	actual = cos(x)
	n = 50
	approximation = [S(i,n)[0] for i in x]
	print 'Approximation for cos(x) using %d terms' % n
	print '%10s %15s %15s' % ('x', 'actual value', 'approximation')
	for i in range(len(approximation)):
		print '%10f %15f %15f' % (x[i], actual[i], approximation[i])

if __name__ == '__main__':
	_test()


'''
Approximation for cos(x) using 50 terms
         x    actual value   approximation
 -5.000000        0.283662        0.283662
 -4.000000       -0.653644       -0.653644
 -3.000000       -0.989992       -0.989992
 -2.000000       -0.416147       -0.416147
 -1.000000        0.540302        0.540302
  0.000000        1.000000        1.000000
  1.000000        0.540302        0.540302
  2.000000       -0.416147       -0.416147
  3.000000       -0.989992       -0.989992
  4.000000       -0.653644       -0.653644
'''
