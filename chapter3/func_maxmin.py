def maxmin(f, a, b, n=1000):
	'''
	Finds the maximum and minimum of the function f on the interval
	[a,b] among n uniformly spaced points.

	The function returns a tuple (max, min)
	'''

	dx = (a-b)/float(n)
	x = [a + i*dx for i in range(n+1)]
	y = [f(i) for i in x]
	return max(y), min(y)

from math import cos, pi
print maxmin(cos, -pi/2, 2*pi, 100001)

'''
python func_maxmin.py
(0.99999999950652962, -1.0)
'''
