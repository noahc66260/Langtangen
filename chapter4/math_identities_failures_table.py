# I have omitted the identity exp(a+b) = exp(a)*exp(b) because of
# an overflow error for the second set of limits
# I have also omitted log(a**b) = b*log(a) and 
# sinh(a+b) = (exp(a)*exp(b)-exp(-a)*exp(-b))/2.0 for the same reasons

# Furthermore, the is a typo in the question that leads to a ValueError
# Specifically, A should never be negative, or else log(a*b) could be negative
# and we know the log of a negative number does not exist. 
# I have changed things so that A=1E-7 rather than A=-1E+7

from math_identities_failures_cml import *
from math import *
from scitools.StringFunction import StringFunction
functions = ( \
('a - b', '-(b-a)'),\
('a/b', '1/(b/a)'),\
('(a*b)**4', 'a**4*b**4'),\
('(a+b)**2', 'a**2 + 2*a*b + b**2'),\
('(a+b)*(a-b)', 'a**2 - b**2'),\
('log(a*b)', 'log(a) + log(b)'),\
('a*b', 'exp(log(a) + log(b))'),\
('1/(1/a + 1/b)', 'a*b/(a+b)'),\
('a*(sin(b)**2+cos(b)**2)', 'a'),\
('tan(a+b)', 'sin(a+b)/cos(a+b)'),\
('sin(a+b)', 'sin(a)*cos(b)+sin(b)*cos(a)')
)

print '%30s %30s %5s %5s %15s' % ('expression 1','expression 2', 'A', 'B', 'Success Rate')
A = 0
B = 1
for i in functions:
	fn1 = StringFunction(i[0], independent_variables=('a','b'))
	fn2 = StringFunction(i[1], independent_variables=('a','b'))
	x = equal(fn1, fn2, A, B)
	print '%30s %30s %5d %5d %15f' % (i[0], i[1], A, B, x)
print '%30s %30s %5s %5s %15s' % ('expression 1','expression 2', 'A', 'B', 'Success Rate')
A = 1E-7
B = 1E+7
for i in functions:
	fn1 = StringFunction(i[0], independent_variables=('a','b'))
	fn2 = StringFunction(i[1], independent_variables=('a','b'))
	x = equal(fn1, fn2, A, B)
	print '%30s %30s %5g %5g %15f' % (i[0], i[1], A, B, x)

