import sys
from scitools.std import *
import scitools.filetable as ft
usage = '%s dt k\nk > 1' % sys.argv[0]

try:
	dt = float(sys.argv[1])
	k = int(sys.argv[2])
except:
	print usage
	sys.exit(1)

def v(dt,k,a):
	'''
	Uses the Trapezoidal rule to calculate the velocity
	at time step k (each time step is dt) from discrete measurements
	of acceleration
	k specifices the time to measure velocity (k * dt)
	dt is the time step 
	a is the list of acceleration measurements
	
	The function returns a velocity
	'''
	# note: k < len(a)
	return dt*(1./2*a[0] + 1./2*a[-1] + sum(a[1:k]))
	

filename = 'acc.dat'
infile = open(filename, 'r')
accel = ft.read_columns(infile)[0]
infile.close()
print 'v(t_k) = %f' % (v(dt, k, accel))
plot(range(len(accel)),accel,
	xlabel='Units of time elapsed (delta t)',
	ylabel='Accelaration m/s^2',
	title='Acceleration v. Time')
raw_input('Press Enter to quit: ')

'''
python acc2vel_v1.py .5 40
v(t_k) = 9.839308
Press Enter to quit: 
'''
