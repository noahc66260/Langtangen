from scitools.std import *
import glob, os
for filename in glob.glob('tmp*.png'):
	os.remove(filename)

A1 = 15 # degrees C
A2 = 7 # degrees C
P1 = 365*24*60*60 # seconds
P2 = 24*60*60 # seconds
w1 = 2.*pi/P1 # note: the book has a type and says w1 = 2*pi*P1
w2 = 2.*pi/P2
k = 10**-6 # m**2/s, the heat conduction coefficient
a1 = sqrt(w1/(2.*k))
a2 = sqrt(w2/(2.*k))
T0 = 10 # degrees C

def T(z,t):
	'''
	Formula for temperature oscillations in the 
	ground.
	A1 is the amplitude of annual variations, in deg C
	A2 is the amplitude of the day/night variations in deg C
	w1 = 2*pi*P1
	w2 = 2*pi*P2
	a1 = sqrt(w1/(2.*k))
	a2 = sqrt(w2/(2.*k))
	k is the heat conduction coefficient
	T0 is the initial temperature
	z is the depth in the ground (m)
	t is the time in seconds
	A1, A2, w1, w2, a1, a2, k, T0 are global variables
	'''
	from scitools.std import exp, sin
	return T0 + A1*exp(-a1*z)*sin(w1*t-a1*z) \
		+ A2*exp(-a2*z)*sin(w2*t-a2*z)

z = linspace(0,1,1000)
t = linspace(0,3*P2,31) # increments of P2/10.
counter = 0
for i in t:
	plot(z,T(z,i),
		axis=[z[0], z[-1], 0, 20],
		xlabel='z (meters)',
		ylabel='Temperature (C)',
		legend='t = %.2f hours' % (i/3600.),
		savefig='tmp%04d' % counter)
	counter += 1
movie('tmp*.png', encoder='convert', fps=3, output_file='exercise_5.23.gif')

