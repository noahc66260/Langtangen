import glob, os
for filename in glob.glob('tmp*.png'):
	os.remove(filename)
from scitools.std import *

def H(x,e):
	'''
	A smooth, continuous version of the Heaviside function
	evaluated at x.
	e is epsilon, of which we transition from 0 to 1 from
	-e <= x <= e
	'''
	from scitools.std import pi, sin
	# we must use there where() fn since x may be an array
	import operator
	condition = operator.and_(-e <= x, x <= e)
	i = where(x > e, 1, x)
	i = where(condition, 1./2 + x/(2.*e) + 1./(2*pi)*sin(pi*x/e), i)
	i = where(x < -e, 0, i)
	return i

x = linspace(-1,1,1000)
e = linspace(1,0,30)
counter = 0
for i in e:
	plot(x,H(x,i), axis=[x[0], x[-1], -.15, 1.15], xlabel='x',
		ylabel='y', legend='e = %4.3f' % i,
		savefig='tmp%04d.png' % counter)
	counter += 1
movie('tmp*.png', encoder='convert', fps=3, output_file='exercise_5.22.gif')

