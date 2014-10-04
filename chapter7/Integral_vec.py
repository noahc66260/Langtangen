def trapezoidal_vectorized(f, a, x, n):
	h = (x-a)/float(n)
	I = 0.5*f(a)
	from scitools.std import array
	s = f(a + array(range(1,n))*h)
	I += sum(s)
	I += 0.5*f(x)
	I *= h
	return I

def trapezoidal(f, a, x, n):
	h = (x-a)/float(n)
	I = 0.5*f(a)
	from scitools.std import iseq
	for i in iseq(1, n-1):
		I += f(a + i*h)
	I += 0.5*f(x)
	I *= h
	return I

class Integral1:
	def __init__(self, f, a, n=100):
		self.f, self.a, self.n = f,a,n
		
	def __call__(self, x):
		return trapezoidal_vectorized(self.f, self.a, x, self.n)

class Integral2:
	def __init__(self, f, a, n=100):
		self.f, self.a, self.n = f,a,n
		
	def __call__(self, x):
		return trapezoidal(self.f, self.a, x, self.n)

class Integral3:
	def __init__(self, f, a, n=100):
		self.f, self.a, self.n = f,a,n
		
	def __call__(self, x):
		from numpy import vectorize
		t = vectorize(trapezoidal)
		return t(self.f, self.a, x, self.n)


def _test():
	from scitools.std import sin, pi
	s1 = Integral1(sin, 0)
	s2 = Integral2(sin, 0)
	s3 = Integral3(sin, 0)
	import time
	e0 = time.time()
	for i in range(1000):
		s1(pi)
	elapsed_time = time.time() - e0
	print 'elapsed time manual vectorization = %g' % elapsed_time
	e0 = time.time()
	for i in range(1000):
		s2(pi)
	elapsed_time = time.time() - e0
	print 'elapsed time no vectorization =     %g' % elapsed_time
	e0 = time.time()
	for i in range(1000):
		s3(pi)
	elapsed_time = time.time() - e0
	print 'elapsed time numpy vectorization =  %g' % elapsed_time

if __name__ == '__main__':
	_test()

'''
python Integral_vec.py
elapsed time manual vectorization = 0.505458
elapsed time no vectorization =     1.26636
elapsed time numpy vectorization =  5.55135
'''
