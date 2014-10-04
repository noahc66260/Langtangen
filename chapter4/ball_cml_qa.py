import sys
try:
	v0 = eval(sys.argv[1])
except IndexError:
	v0 = eval(raw_input('v=? '))	
try:
	t = eval(sys.argv[2])
except IndexError:
	t = eval(raw_input('t=? '))	
g = 9.81
y = v0*t -0.5*g*t**2
print y

'''
python ball_cml.py 5 3
-29.145
'''

