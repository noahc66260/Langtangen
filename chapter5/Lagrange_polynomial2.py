from Lagrange_polynomial1 import *
from scitools.std import *

def graph(f, xmin, xmax, n, resolution=1001):
	'''
	This function graphs the Lagrange interpolation formula
	for the function f between xmin and xmax using different
	values of n, which is to say sets of equally spaced points
	over the domain [xmin, xmax] containing n points for 
	varying values of n.
	The resolution is for the number of points we interpolate
	when we graph it.
	
	f is a function
	xmin <= xmax
	n is a list
	resolution > 0
	'''
	#from Lagrange_polynomial1 import *
	#from scitools.std import *
	figure()
	hold('on')
	Lpoints = zeros((resolution, len(n))) # f(x) interpolation values
	xlist = linspace(xmin, xmax, resolution)
	plot(xlist, f(xlist))
	legend('f(x)')
	axis([xmin, xmax, min(f(xlist)), max(f(xlist))])
	for i in n:
		x = linspace(xmin, xmax, i)
		y = f(x)
		points = array(zip(x,y))
		for j in range(resolution):
			Lpoints[j,n.index(i)] = Lagrange(xlist[j], points)
		plot(xlist, Lpoints[:,n.index(i)])
		legend('n = %d' % i)
		#hold('on')

f = lambda x: abs(x)
n = [2,4,6,10]
xmin = -2
xmax = 2
graph(f, xmin, xmax, n)
raw_input('Press Enter to quit: ')
	
