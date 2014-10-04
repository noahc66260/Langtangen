'''
Note: the question asks us to use numpy.float96 and numpy.float32
objects and see how our results change. 
Simply put, the only difference is that using the new kinds of
objects does not evoke an overflow error for our input. 
However, when no overflow error exists, the computation between
the kinds of new objects and our original kind is no different.
So really the difference is that our program is less likely to crash.
'''


import math

def v(x, mu=1E-6, exp=math.exp):
	'''
	A function to calculate the change in air
	velocity along the surface of an object.
	x = 1 is the surface of the object
	x = 0 is some distance away from the object
	mu is related to the viscosity of the air
	exp is a user defined exponential function
	
	The function returns a 3-tuple. 
	numerator, denominator, float(num/denom)
	'''
	numerator = 1 - exp(x/(1.*mu))
	denominator = 1 - exp(1./mu)
	result = (1.*numerator)/denominator
	return numerator, denominator, result

from scitools.std import *
import numpy as np
x = linspace(0,1,20)
exp = ['math.exp', 'np.exp']
mu = 1E-2
print 'for mu = %g' % mu
print '%10s %10s %10s %11s %10s'\
	 % ('function', 'x', 'numerator', 'denominator', 'result')
for i in x:
	for j in exp:
		a = v(i,mu,eval(j))
		num = a[0]
		denom = a[1]
		result = a[2]
		print '%10s %10.3f %10.2g %11.2g %10.2g' \
			% (j, i, num, denom, result)

mu = float96([1,0.01,0.001]) # will not cause overflow
x = float96(linspace(0,1,10000))
figure()
axis([float(x[0]-.1),float(x[-1]+.1),-.1,1.1])
	# for some reason use of the numpy.float96 type is unrecognizable
	# when used as argument to axis
xlabel('x')
ylabel('v(x)')
hold('on')
for i in mu:
	plot(x,v(x,i,np.exp)[-1])
	legend('mu = %.4f' % i)
raw_input('Press Enter to quit: ')


'''
for mu = 0.01
  function          x  numerator denominator     result
  math.exp      0.000          0    -2.7e+43         -0
    np.exp      0.000          0    -2.7e+43         -0
  math.exp      0.053   -1.9e+02    -2.7e+43    7.1e-42
    np.exp      0.053   -1.9e+02    -2.7e+43    7.1e-42
  math.exp      0.105   -3.7e+04    -2.7e+43    1.4e-39
    np.exp      0.105   -3.7e+04    -2.7e+43    1.4e-39
  math.exp      0.158   -7.2e+06    -2.7e+43    2.7e-37
    np.exp      0.158   -7.2e+06    -2.7e+43    2.7e-37
  math.exp      0.211   -1.4e+09    -2.7e+43    5.2e-35
    np.exp      0.211   -1.4e+09    -2.7e+43    5.2e-35
  math.exp      0.263   -2.7e+11    -2.7e+43      1e-32
    np.exp      0.263   -2.7e+11    -2.7e+43      1e-32
  math.exp      0.316   -5.2e+13    -2.7e+43    1.9e-30
    np.exp      0.316   -5.2e+13    -2.7e+43    1.9e-30
  math.exp      0.368     -1e+16    -2.7e+43    3.7e-28
    np.exp      0.368     -1e+16    -2.7e+43    3.7e-28
  math.exp      0.421   -1.9e+18    -2.7e+43    7.2e-26
    np.exp      0.421   -1.9e+18    -2.7e+43    7.2e-26
  math.exp      0.474   -3.7e+20    -2.7e+43    1.4e-23
    np.exp      0.474   -3.7e+20    -2.7e+43    1.4e-23
  math.exp      0.526   -7.2e+22    -2.7e+43    2.7e-21
    np.exp      0.526   -7.2e+22    -2.7e+43    2.7e-21
  math.exp      0.579   -1.4e+25    -2.7e+43    5.2e-19
    np.exp      0.579   -1.4e+25    -2.7e+43    5.2e-19
  math.exp      0.632   -2.7e+27    -2.7e+43      1e-16
    np.exp      0.632   -2.7e+27    -2.7e+43      1e-16
  math.exp      0.684   -5.2e+29    -2.7e+43    1.9e-14
    np.exp      0.684   -5.2e+29    -2.7e+43    1.9e-14
  math.exp      0.737     -1e+32    -2.7e+43    3.7e-12
    np.exp      0.737     -1e+32    -2.7e+43    3.7e-12
  math.exp      0.789   -1.9e+34    -2.7e+43    7.2e-10
    np.exp      0.789   -1.9e+34    -2.7e+43    7.2e-10
  math.exp      0.842   -3.7e+36    -2.7e+43    1.4e-07
    np.exp      0.842   -3.7e+36    -2.7e+43    1.4e-07
  math.exp      0.895   -7.2e+38    -2.7e+43    2.7e-05
    np.exp      0.895   -7.2e+38    -2.7e+43    2.7e-05
  math.exp      0.947   -1.4e+41    -2.7e+43     0.0052
    np.exp      0.947   -1.4e+41    -2.7e+43     0.0052
  math.exp      1.000   -2.7e+43    -2.7e+43          1
    np.exp      1.000   -2.7e+43    -2.7e+43          1
'''	
