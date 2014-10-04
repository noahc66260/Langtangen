import sys
usage = '%s v0 t' % sys.argv[0]
try:
	v0 = eval(sys.argv[1])
	t = eval(sys.argv[2])
except:
	print usage
	sys.exit(1)
g = 9.81
y = v0*t -0.5*g*t**2
print y

'''
python ball_cml.py 5 3
-29.145
'''

