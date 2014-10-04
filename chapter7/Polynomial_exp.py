from Polynomial import *
import sys
usage = '%s x N [N2 N3 ...]' % sys.argv[0]
try:
	x = float(sys.argv[1])
	N = (sys.argv[2:])
	for i in range(len(N)):
		N[i] = int(N[i])
except:
	print usage
	sys.exit(1)

print 'Our function is the exponential function'
print 'x = %f' % x
from math import factorial, exp
for i in N:
	poly = [1./factorial(j) for j in range(0,i)]
	p = Polynomial(poly)
	print 'First %2d' % i, 'terms approximation: %.6f' % p(x)

print 'exact value: %.6f' % exp(x)

'''
python Polynomial_exp.py .5 2 5 10 15 25
Our function is the exponential function
x = 0.500000
First  2 terms approximation: 1.500000
First  5 terms approximation: 1.648438
First 10 terms approximation: 1.648721
First 15 terms approximation: 1.648721
First 25 terms approximation: 1.648721
exact value: 1.648721

python Polynomial_exp.py 3 2 5 10 15 25
Our function is the exponential function
x = 3.000000
First  2 terms approximation: 4.000000
First  5 terms approximation: 16.375000
First 10 terms approximation: 20.063393
First 15 terms approximation: 20.085523
First 25 terms approximation: 20.085537
exact value: 20.085537

python Polynomial_exp.py 10 2 5 10 15 25
Our function is the exponential function
x = 10.000000
First  2 terms approximation: 11.000000
First  5 terms approximation: 644.333333
First 10 terms approximation: 10086.573192
First 15 terms approximation: 20188.170595
First 25 terms approximation: 22025.431666
exact value: 22026.465795
'''
