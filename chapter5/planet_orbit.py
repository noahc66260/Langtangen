from scitools.std import *
import glob, os
for filename in glob.glob('tmp*.png'):
	os.remove(filename)

a = 1 # semimajor axis of ellipse
b = 1 # semiminor axis of ellipse
w = 1 # angular velocity of planet around star

n = 50
dt = 2.*pi/(w*n)
tk = linspace(0,n*dt,n+1)
x = a*cos(w*tk)
y = b*sin(w*tk)

v = lambda w, a, b, t: w*sqrt(a**2 * sin(w*t)**2 + b**2 * cos(w*t)**2)
# v is the magnitude of the angular velocity

counter = 0
for k in range(n+1):
	plot(x[0:k+1], y[0:k+1],
		x[k:k+1], y[k:k+1],'o',
		axis=[-a*1.05, a*1.05, -b*1.05, b*1.05],
		xlabel='x',
		ylabel='y',
		title='Instantaneous velocity = %f units/second' \
			% v(w,a,b,tk[k]),
		savefig='tmp%04d.png' % counter)
	counter += 1
movie('tmp*.png', encoder='convert', fps=2, output_file='exercise_5.26.gif')

