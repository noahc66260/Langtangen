import sys
from scitools.std import *
usage = '%s y0 theta v0\ntheta is in radians' % (sys.argv[0])
try:
	y0 = float(sys.argv[1])
	theta = float(sys.argv[2])
	v0 = float(sys.argv[3])
except:
	print usage
	sys.exit(1)

def f(x):
	'''
	Calculates the height of a projectile at a given
	horizontal distance.
	theta, v0, and y0 are global variables
	'''
	from scitools.std import tan, cos
	g = 9.81 # m/s**2
	y = x*tan(theta) - 1./(2*v0**2)*(g*x**2)/(cos(theta)**2) + y0
	return y

g = 9.81
x = linspace(0, sin(2*theta)*v0**2.0/g, 100)
y = f(x)
plot(x,y,xlabel='x', ylabel='y', title='Trajectory of a ball')
raw_input('Press Enter to quit: ')

