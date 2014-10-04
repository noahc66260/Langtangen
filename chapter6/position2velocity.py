from scitools.std import *
import scitools.filetable as ft
def v_pos(k,x,s):
	'''
	Simple formula for calculating velocity in one dimension
	for an array with positions recorded in increments of
	time step s
	0 <= k < len(x)-1

	The function returns the one-dimensional velocity 
	'''
	return (x[k+1] - x[k])/float(s)

filename = 'pos.dat'
infile = open(filename, 'r')
s = float(infile.readline())
x,y = ft.read_columns(infile)
infile.close()

t = [s*i for i in range(0,len(x))]
vx = [0]*(len(x)-1)
vy = [0]*(len(y)-1)
for i in range(len(x)-1):
	vx[i] = v_pos(i,x,s)
	vy[i] = v_pos(i,y,s)

figure()
plot(t[:-1],vx,
	xlabel='Time (s)',
	ylabel='Velocity in x-direction',
	title='V_x v. time')

figure()
plot(t[:-1], vy,
	xlabel='Time (s)',
	ylabel='Velocity in y-direction',
	title='V_y v. time')

raw_input('Press Enter to quit: ')
