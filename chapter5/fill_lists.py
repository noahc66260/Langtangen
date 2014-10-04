from scitools.std import *
x = linspace(-4,4,50)

def h(x):
	''' 
	Calculates the density of the normal distribution
	with mean = 0 and standard deviation = 1
	'''
	from numpy import sqrt, exp, pi
	return 1/sqrt(2*pi)*exp(-.5*x**2)

y = h(x)
plot(x,y)
raw_input('Hit enter to quit: ')

