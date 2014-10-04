import sys
from scitools.std import *

usage = '%s m v0' % sys.argv[0]
try:
	m = eval(sys.argv[1])
	v0 = eval(sys.argv[2])
except:
	print usage
	sys.exit(1)

g = 9.81 # m/s**2
y = lambda t: v0*t - 0.5*g*t**2
v = lambda t: v0 - g*t
P = lambda y: m*g*y
K = lambda v: .5*m*v**2
t = linspace(0,2.*v0/g,200)
position = y(t)
velocity = v(t)
potential_energy = P(position)
kinetic_energy = K(velocity)

figure()
hold('on')
plot(t,potential_energy, 
	t,kinetic_energy, 
	t,potential_energy+kinetic_energy,
	xlabel='time (s)',
	ylabel='energy (J)',
	legend=['PE', 'KE', 'PE + KE'],
	axis=[t[0], t[-1], -max(kinetic_energy)*.05, max(kinetic_energy)*1.05])
raw_input('Press Enter to quit: ')

