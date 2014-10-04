import random
import sys
A = -100
B = 100
x = float(sys.argv[1])
epsilon = 1E-10
fc1 = 0 # failure count for (a*b)**3 = a**3*b**3
fc2 = 0 # failure count for a/b = 1/(b/a)

for i in range(int(x)):
	a = random.uniform(A,B)
	b = random.uniform(A,B)
	if abs((a*b)**3 - a**3*b**3) >= epsilon:
		fc1 += 1
	if abs(a/b - 1/(b/a)) >= epsilon:
		fc2 += 1
print '(a*b)**3 == a**3*b**3 %.1f percent of the time' % ((1-float(fc1)/x)*100)
print 'a/b == 1/(b/a) %.1f percent of the time' % ((1-float(fc2)/x)*100)

'''
python math_identities_failures.py 10000
n math_identities_failures.py 10000
(a*b)**3 == a**3*b**3 36.5 percent of the time
a/b == 1/(b/a) 100.0 percent of the time
'''
