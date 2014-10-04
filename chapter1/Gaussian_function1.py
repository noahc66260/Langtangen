m = 0 # the mean
x = 1 # the argument
s = 2 # the standard deviation

from math import sqrt, pi, exp
f = 1./(sqrt(2*pi)*s) * exp(-1./2 * (float(x - m)/s)**2)

print """The value of the Gaussian distribution for
m = %d, x = %d, and s = %d is %f""" % (m, x, s, f)
 
'''
Verified to be 0.176033 by Mathematica
'''
