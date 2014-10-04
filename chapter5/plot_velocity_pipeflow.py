def v(r, beta, mu0, R, n):
	'''
	Computes the velocity of a fluid through a long pipe
	R is the radius of the pipe
	r is the radius at which we measure fluid flow (0 <= r <= R)
	n is a real number reflecting the viscous properties of the fluid
	beta is the pressure gradient
	mu0 is a viscosity coefficient
	'''
	return (beta/(2.*mu0))**(1./n) \
		* n/(n+1.) \
		* (R**(1+1./n) - r**(1+1./n))

from scitools.std import *
R = 1
beta = 0.02
mu = 0.02
n = 0.1
r = linspace(0,R,500)

import os, glob
for filename in glob.glob('tmp*.png'):
	os.remove(filename)

counter = 0
n = linspace(1,0.01,50)
maxy = v(0,beta,mu,R,1)
for i in n:
	plot(r,v(r,beta,mu,R,i),
		xlabel='r',
		ylabel='velocity',
		axis=[r[0], r[-1], -0.05, maxy*1.05],
		legend='n = %.2f' % i,
		savefig='tmp%04d.png' % counter)
	counter += 1
movie('tmp*.png', encoder='convert', fps=3, output_file='exercise_5.28.gif')	
