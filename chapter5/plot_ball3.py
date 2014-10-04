import sys
from scitools.std import *

usage = '%s initial_velocity' % (sys.argv[0])
try:
	v0 = float(sys.argv[1])
except:
	print usage
	sys.exit(1)
g = 9.81 # m/s**2
t = linspace(0, 2.0*v0/g, 50)
f = lambda t: v0*t - 0.5*g*t**2
y = f(t)

plot(t,y,
	xlabel='time (s)', 
	ylabel='height (m)', 
	axis=[min(t), max(t), min(y), max(y)*1.05])
raw_input('Press Enter to quit: ')

