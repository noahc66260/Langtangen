import glob, os
for filename in glob.glob('tmp*.png'):
	os.remove(filename)
from scitools.std import *

def f(x,t):
	'''
	Computes the function of a wave packet localized in space
	'''
	return exp(-(x-3*t)**2)*sin(3*pi*(x-t))

x = linspace(-6,6,1001)
t = linspace(-1,1,61)
figure()
counter = 0
for i in t:
	plot(x,f(x,i), axis=[x[0], x[-1], 0, 1], xlabel='x', 
		ylabel='f(x,t)', legend='t = %4.2f' % i,
		savefig='tmp%04d.png' % counter)
	counter += 1
movie('tmp*.png', encoder='convert', fps=6, output_file='exercise_5.21.gif')

