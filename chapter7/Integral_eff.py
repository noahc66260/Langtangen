def trapezoidal(f, a, x, n):
	from scitools.std import array, iseq, linspace, zeros
	x = array(x)
	I = zeros(len(x))
	index = 0
	new_sum = 0
	old_sum = 0
	for i in x:
		new_sum = 0.5*f(a)
		h = (i-a)/float(n)
		new_sum += sum(f(a + array(range(1,n))*h))
		new_sum += 0.5*f(i)
		new_sum *= h
		new_sum += old_sum
		I[index] = new_sum
		index += 1
		a = i
		old_sum = new_sum	
	if len(I) == 1:
		return I[0]
	else:
		return I

class Integral:
	def __init__(self, f, a, n=100):
		self.f, self.a, self.n = f,a,n
		
	def __call__(self, x):
		return trapezoidal(self.f, self.a, x, self.n)

def _test():
	from scitools.std import sin, pi, array
	s = Integral(sin, 0)
	x = array([pi/4, pi/2, 3*pi/4, pi])
	a = s(x)
	print 'The integral of sin(x) for'
	for i in range(4):
		print '0 to %.2f' % x[i], 'is %.2f' % a[i]

if __name__ == '__main__':
	_test()

'''
python Integral_eff.py
The integral of sin(x) for
0 to 0.79 is 0.29
0 to 1.57 is 1.00
0 to 2.36 is 1.71
0 to 3.14 is 2.00
'''
