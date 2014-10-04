class Quadratic:
	def __init__(self, a = 0, b = 0, c = 0):
		self.a = a
		self.b = b
		self.c = c

	def value(self, x):
		a = self.a
		b = self.b
		c = self.c
		return a*x**2 + b*x + c

	def table(self, n, l, r):
		from scitools.std import linspace, array
		x = linspace(l, r, n)
		print '%10s %10s' % ('x', 'f(x)')
		for i in x:
			print '%10f %10f' % (i, value(i))

	def roots(self):
		a = self.a
		b = self.b
		c = self.c
		delta = b**2 - 4*a*c
		if delta < 0:
			from cmath import sqrt
		elif delta > 0:
			from math import sqrt
		r1 = (-b + sqrt(delta))/float(2*a)
		r2 = (-b - sqrt(delta))/float(2*a)
		return r1, r2

def _test():
	a, b, c = 1, 5, 6
	q1 = Quadratic(a, b, c)
	r1, r2 = q1.roots()
	print 'The root of a*x**2 + b*x + c for'
	print 'a=%f' % (a)
	print 'b=%f' % (b)
	print 'c=%f' % (c)
	print 'is', r1, 'and', r2
	print 'The value of the polynomial at', r1, 'is', q1.value(r1)
	
	a, b, c = 1, 1, 6
	q1 = Quadratic(a, b, c)
	r1, r2 = q1.roots()
	print 'The root of a*x**2 + b*x + c'
	print 'a=%f' % (a)
	print 'b=%f' % (b)
	print 'c=%f' % (c)
	print 'is', r1, 'and', r2
	print 'The value of the polynomial at', r1, 'is', q1.value(r1)

if __name__ == '__main__':
	_test()

'''
The root of a*x**2 + b*x + c for
a=1.000000
b=5.000000
c=6.000000
is -2.0 and -3.0
The value of the polynomial at -2.0 is 0.0
The root of a*x**2 + b*x + c
a=1.000000
b=1.000000
c=6.000000
is (-0.5+2.39791576166j) and (-0.5-2.39791576166j)
The value of the polynomial at (-0.5+2.39791576166j) is (8.881784197e-16+0j)
'''
