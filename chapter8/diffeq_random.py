from scitools.std import *

a = 8121
c = 28411
m = 134456

def generate_numbers(a, c, m, N, x0):
	'''
	Generates two arrays, x and y of length N,
	using the difference equations specified 
	in equation (8.14) and (8.15).
	The y array contains our pseudorandom numbers
	The function returns y
	'''
	x = zeros(N)
	y = zeros(N)
	x[0] = x0
	y[0] = float(x[0])/m
	for i in range(1,N):
		x[i] = (a * x[i-1] + c) % m
		y[i] = float(x[i])/m 
	return y

N = 10**6
x0 = 1
y = generate_numbers(a,c,m,N,x0)
pos, freq = compute_histogram(y)
plot(pos, freq)
raw_input('Press Enter to quit: ')

