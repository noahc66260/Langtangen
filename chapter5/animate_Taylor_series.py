#import os, glob
#for filename in glob.glob('tmp*.png'):
#	os.remove(filename)

from scitools.std import *
def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):
	'''
	Computes the power series approximation of a function
	fk is the function inside the summation
	M is the lower index which we sum from
	N is the upper index which we sum to
	xmin, xmax, ymin, ymax is the plotting range for graphing
	n is the number of points which we plot
	exact is the function we are approximating
	'''
	import os, glob
	for filename in glob.glob('tmp*.png'):
		os.remove(filename)

	x = linspace(xmin, xmax, n)
	y = exact(x)
	counter = 0
	approx = zeros(n)
	for i in range(M, N+1):
		approx += fk(x,i)
		plot(x, approx,
			x, y,
			axis=[xmin, xmax, ymin, ymax],
			xlabel='x',
			ylabel='y',
			legend=['approx: %d terms' % (i-M+1), 'exact'],
			savefig='tmp%04d.png' % counter)
		counter += 1	
	movie('tmp*.png', encoder='convert', fps=2, output_file='exercise_5.27.gif')

# We try this for sin(x)
def test1():
	fk = lambda x,k: (-1)**k * x**(2*k+1) / float(factorial(2*k+1))
	xmin = 0
	xmax = 13*pi
	M = 0
	N = 40
	ymin = -2
	ymax = 2
	n = 500
	exact = lambda x: sin(x)
	animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact)

def test2():
	fk = lambda x,k: (-x)**k/float(factorial(k))
	xmin = 0
	xmax = 15
	M = 0
	N = 30
	ymin = -0.5
	ymax = 1.4
	n = 500
	exact = lambda x: exp(-x)
	animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact)

if __name__ == '__main__':
	#test1()
	test2()
	
