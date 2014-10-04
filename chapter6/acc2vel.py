import sys
from scitools.std import *
import scitools.filetable as ft
usage = '%s dt' % sys.argv[0]

try:
	dt = float(sys.argv[1])
except:
	print usage
	sys.exit(1)

def v(dt,k,v_old,a):
	'''
	Uses the Trapezoidal rule to calculate the velocity
	at time step k (each time step is dt) from discrete measurements
	of acceleration in an efficient manner by using the results
	from previous calculations.
	k specifices the time to measure velocity (k * dt)
	dt is the time step 
	a is the list of acceleration measurements
	
	The function returns a velocity for time step k
	'''
	# note: k < len(a)
	return v_old + dt/2. * (a[k-1] + a[k])
	

filename = 'acc.dat'
infile = open(filename, 'r')
accel = ft.read_columns(infile)[0]
infile.close()

vel = [0]*len(accel)
v0 = 0
vel[0] = v0
for k in range(1,len(accel)):
	vel[k] = v(dt, k, vel[k-1], accel)
plot(linspace(0,(len(vel)-1)*dt,len(vel)),vel,
	xlabel='Time elapsed',
	ylabel='Velocity (m/s)',
	title='Velocity v. Time')
raw_input('Press Enter to quit: ')

'''
'''
