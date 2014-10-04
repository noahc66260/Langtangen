from scitools.std import *

def D(f,x,N):
	a = zeros(N)
	for i in range(N):
		h = 2**(-i)
		a[i] = (f(x+h) - f(x)) / h
	return a

figure()
N = 80
x = 0
a = D(sin, x, N)
plot(range(80), a, 'o')

figure()
x = pi
a = D(sin, x, N)
plot(range(80), a, 'o')
raw_input('Press Enter to quit: ')

'''
Computations may go wrong for large N when there is cancellation
'''
