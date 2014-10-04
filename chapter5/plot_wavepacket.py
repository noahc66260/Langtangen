from scitools.std import *
x = linspace(-4,4,200)

def f(x,t):
	'''
	Computes the function of a wave packet localized in space
	'''
	return exp(-(x-3*t)**2)*sin(3*pi*(x-t))

t = zeros(len(x))
y = f(x,t)
plot(x,y)
raw_input('Press Enter to quit: ')

