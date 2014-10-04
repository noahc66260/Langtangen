from scitools.std import *

def N(x, epsilon=1E-4):
	'''
	Plots the hat function but without the discontinuity at x = 1
	[1-epsilon, 1+epsilon] is the interval which we correct
	for the discontinuity in the derivative by replacing it
	with a cubic function
	'''
	a1 = 1./3*epsilon**-2
	a2 = -a1
	d1 = 1 - epsilon + a1*epsilon**3
	d2 = 1 - epsilon - a2*epsilon**3
	b = 0
	c = 0

	import operator
	r = where(x < 0, 0, x)
	condition = operator.and_(0 <= x, x < 1-epsilon)
	r = where(condition, x, r)
	condition = operator.and_(1-epsilon <= x, x < 1)
	expr = a1*(x-1.)**3 + b*(x-1) + c*(x-1) + d1
	r = where(condition, expr, r)
	condition = operator.and_(1 <= x, x < 1+epsilon)
	expr = a2*(x-1.)**3 + b*(x-1) + c*(x-1) + d2
	r = where(condition, expr, r)
	condition = operator.and_(1+epsilon <= x, x < 2)
	r = where(condition, 2-x, r)
	r = where(x >= 2, 0, r)

	return r

# Note: we need to divide the points we plot since our point of
# interest is at x = 1 where the function changes along a very
# fine granularity. Thus we plot with higher resolution in this
# region so that we may change the axes to view the behavior at this 
# point
e = 1E-4
x1 = linspace(-1,0,2)
y1 = N(x1,e)
x2 = linspace(0,1-e,2)
y2 = N(x2,e)
x3 = linspace(1-e,1+e,500)
y3 = N(x3,e)
x4 = linspace(1+e,2,2)
y4 = N(x4,e)
x5 = linspace(2,3,2)
y5 = N(x5,e)
plot(x1,y1,'r-',
	x2,y2, 'r-',
	x3,y3, 'r-',
	x4,y4, 'r-',
	x5,y5, 'r-')
axis([x1[0],x5[-1], -.05, 1.05])
raw_input('Press Enter to quit: ')
