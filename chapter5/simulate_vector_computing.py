# we simulate the computation of y = cos(sin(x)) + exp(1/t)
# for x = [0,2] and t = [1,1.5]

from math import cos, sin, exp
tmp = sin(0)
tmp = cos(tmp)
tmp += exp(1/1)
y1 = tmp
tmp = sin(2)
tmp = cos(tmp)
tmp += exp(1/1.5)
y2 = tmp
print 'y = [%.2f, %.2f] by hand' % (y1, y2)

# now to error check
from scitools.std import *
x = array([0,2])
t = array([1,1.5])
def y(x,t):
	from scitools.std import cos, sin, exp
	return cos(sin(x)) + exp(1./t)
ylist = y(x,t)
print 'y = [%.2f, %.2f] using the function with vector arguments' % (ylist[0], ylist[1])

'''
python simulate_vector_computing.py
y = [3.72, 2.56] by hand
y = [3.72, 2.56] using the function with vector arguments
'''
