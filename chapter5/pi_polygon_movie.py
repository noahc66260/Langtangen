from scitools.std import *
import glob, os
for filename in glob.glob('tmp*.png'):
	os.remove(filename)

def pathlength(x,y):
	'''                                                                        	Computes the path length of the points (x0,y0), (x1,y1), ..., (xn,yn)      	x is a list of real numbers     
	y is a list of real numbers  
	len(x) and len(y) must be equal                                        
	'''

	from scitools.std import sqrt
	sum = 0
	n = len(x)
	for i in range(1,n):
		sum += sqrt((x[i] - x[i-1])**2 + (y[i] - y[i-1])**2)
	return sum

def pi_approx(N):
	'''
	Calculates the approximation to pi by computing
	the path length of a polygon with N points inscribed
	in the circle of radius 1
	'''
	from scitools.std import sin, pi
	x = [1./2*cos(2.*pi*i/(N)) for i in range(N+1)]
	y = [1./2*sin(2.*pi*i/(N)) for i in range(N+1)]
	approx = pathlength(x,y)
	return approx
	
N = array(range(3,31))
count = 0
C = 1000 # points with which we draw the circle
xcircle = [1./2*cos(2.*pi*i/C) for i in range(C+1)]
ycircle = [1./2*sin(2.*pi*i/C) for i in range(C+1)]
xmin = -.55
xmax = .55
ymin = xmin
ymax = .65
for n in N:
	x = [1./2*cos(2.*pi*i/n) for i in range(n+1)]
	y = [1./2*sin(2.*pi*i/n) for i in range(n+1)]
	plot(x,y,'-o-', xcircle, ycircle,
		axis=[xmin, xmax, ymin, ymax],
		xlabel='x',
		ylabel='y',
		legend='n = %2d, approximation = %7f' % (n, pi_approx(n)),
		savefig='tmp%04d.png' % count)
	count += 1
movie('tmp*.png', encoder='convert', fps=3.3, output_file='exercise_5.25.gif')
