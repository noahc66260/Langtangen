class Spring:
	def __init__(self, k):
		self.k = k

	def force(self, x):
		return self.k*x

	def energy(self,x):
		return 1./2 * self.k * x**2

def table(f,a,b,n, heading=''):
	"""Write out f(x) for x in [a,b] with steps h=(b-a)/n."""
	print heading
	h = (b-a)/float(n)
	for i in range(n+1):
		x = a + i*h
		print 'function value = %10.4f at x = %g' % (f(x), x)

def _test():
	s = Spring(1)
	print 'for Spring.force()'
	table(s.force, 0, 5, 5)
	print ''
	print 'for Spring.energy()'
	table(s.energy, 0, 5, 5)

if __name__ == '__main__':
	_test()

'''
python Spring.py
for Spring.force()

function value =     0.0000 at x = 0
function value =     1.0000 at x = 1
function value =     2.0000 at x = 2
function value =     3.0000 at x = 3
function value =     4.0000 at x = 4
function value =     5.0000 at x = 5

for Spring.energy()

function value =     0.0000 at x = 0
function value =     0.5000 at x = 1
function value =     2.0000 at x = 2
function value =     4.5000 at x = 3
function value =     8.0000 at x = 4
function value =    12.5000 at x = 5
'''
