from scitools.std import *

def a(n):
	from scitools.std import zeros
	arr = zeros(n)
	cum_sum = 0
	for i in range(n):
		k = i + 1
		cum_sum += 4. * (-1)**(k+1) / (2*k-1)
		arr[i] = cum_sum
	return arr
		
def b(n):
	from scitools.std import sqrt, zeros
	arr = zeros(n)
	cum_sum = 0
	for i in range(n):
		k = i + 1
		cum_sum = sqrt(cum_sum**2 + 6 * k**(-2))
		arr[i] = cum_sum
	return arr

def c(n):
	from scitools.std import zeros
	arr = zeros(n)
	cum_sum = 0
	for i in range(n):
		k = i + 1
		cum_sum = (cum_sum**4 + 90 * k**(-4))**(.25)
		arr[i] = cum_sum
	return arr

def d(n):
	from scitools.std import zeros, sqrt
	arr = zeros(n)
	cum_sum = 6 / sqrt(3)
	for i in range(n):
		k = i + 1
		cum_sum += 6 / sqrt(3) * (-1)**k / (3**k * (2*k+1))
		arr[i] = cum_sum
	return arr

def e(n):
	from scitools.std import zeros
	arr = zeros(n)
	cum_sum = 16. / 5 - 4. / 239
	for i in range(n):
		k = i + 1
		cum_sum += 16.*(-1)**k / (5**(2*k+1) * (2*k+1)) \
				- 4. * (-1)**k / (239**(2*k+1) * (2*k+1))
		arr[i] = cum_sum
	return arr

N = 25
x = range(1,N+1)
plot(x,a(N),
	x, b(N),
	x, c(N),
	x, d(N),
	x, e(N),
	legend=['a(n)', 'b(n)', 'c(n)', 'd(n)', 'e(n)'],
	title='Sequences of series which converge to Pi',
	xlabel='n',
	axes=[1,N, 0, 2*pi])
raw_input('Press Enter to quit: ')



