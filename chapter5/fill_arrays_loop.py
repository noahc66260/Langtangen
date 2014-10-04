from scitools.std import *
x = [-4 + i*8./49 for i in range(50)]

def h(x):
	''' 
	Calculates the density of the normal distribution
	with mean = 0 and standard deviation = 1
	'''
	from numpy import sqrt, exp, pi
	return 1/sqrt(2*pi)*exp(-.5*x**2)

y = [h(i) for i in x]
plot(x,y) # x and y can be lists when used as arguments
raw_input('Hit enter to quit: ')

