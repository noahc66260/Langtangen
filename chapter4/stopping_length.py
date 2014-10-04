import sys
usage = '%s v0 mu\nv0 in km/hr' % sys.argv[0]
try:
	v0 = eval(sys.argv[1])
	mu = eval(sys.argv[2])
except:
	print usage
	sys.exit(1)
v0_ms = v0 / 3.6 #convert km/h to m/s
g = 9.81
d = 0.5*v0**2/(mu*g)
print 'Braking distance is %f m' % d

'''
python stopping_length.py 60 1
Braking distance is 183.486239 m
'''

