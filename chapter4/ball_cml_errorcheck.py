import sys
usage = '%s v0 t' % sys.argv[0]
try:
	v0 = eval(sys.argv[1])
	t = eval(sys.argv[2])
except:
	print usage
	sys.exit(1)
g = 9.81
if not 0 < t < 2*v0/g:
	print 't must be between 0 and 2*v0/g = %.2f' % (2*v0/g)	
	sys.exit(1)
y = v0*t -0.5*g*t**2
print y

'''
'''

