from scitools.std import *

def S(x,n):
	'''
	Computes the first n+1 terms of the power series
	for sin(x).
	'''
	from scitools.std import factorial
	sum = 0
	for i in range(n+1):
		sum += (-1)**i * x**(2*i+1) / float(factorial(2*i+1))
	return sum

x = linspace(0, 4*pi, 100)
n = [1,2,3,6,12]
figure()
axis([0, 4*pi, -1.2, 1.2])
hold('on')
for i in n:
	plot(x,S(x,i))
	legend('n = %d' % i)
plot(x, sin(x), '--')
legend('sin(x)')
xlabel('x')
ylabel('y')
title('Approximation of sin(x) using first n terms of power series')
raw_input('Press Enter to quit: ')
	
