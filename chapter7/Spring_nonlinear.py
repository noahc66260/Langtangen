class Spring_Nonlinear:
	def __init__(self, k):
		self.k = k
	def force(self, x):
		return self.k * x
	def energy(self, x):
		f = lambda x: self.k * x
		i = Integral(f,0)
		return i(x)
	

class Integral:
	def __init__(self, f, a, n=100):
		self.f, self.a, self.n = f,a,n

	def __call__(self,x):
		return self._trapezoidal(self.f, self.a, x, self.n)

	def _trapezoidal(self,f,a,x,n):
		from scitools.std import iseq
		h = (x-a)/float(n)
		I = 0.5*f(a)
		for i in iseq(1, n-1):
			I += f(a + i*h)
		I += 0.5*f(x)
		I *= h
		return I

def table(f,a,b,n, heading=''):
	"""Write out f(x) for x in [a,b] with steps h=(b-a)/n."""
	print heading
	h = (b-a)/float(n)
	for i in range(n+1):
		x = a + i*h
		print 'function value = %10.4f at x = %g' % (f(x), x)


def _test():
	s = Spring_Nonlinear(1)
	print 'for Spring_Nonlinear.force()'
	table(s.force, 0, 5, 5)
	print ''
	print 'for Spring_Nonlinear.energy()'
	table(s.energy, 0, 5, 5)

if __name__ == '__main__':
	_test()

'''
python Spring_nonlinear.py
for Spring_Nonlinear.force()

function value =     0.0000 at x = 0
function value =     1.0000 at x = 1
function value =     2.0000 at x = 2
function value =     3.0000 at x = 3
function value =     4.0000 at x = 4
function value =     5.0000 at x = 5

for Spring_Nonlinear.energy()

function value =     0.0000 at x = 0
function value =     0.5000 at x = 1
function value =     2.0000 at x = 2
function value =     4.5000 at x = 3
function value =     8.0000 at x = 4
function value =    12.5000 at x = 5
'''
