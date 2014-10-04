class F:
	def __init__(self, f, xi):
		self.xi = xi
		self.f = f
	def __call__(self, gamma):
		return self.f(gamma) - self.xi

class dFdx:
	def __init__(self, F1, h=1E-6):
		self.F1 = F1
		self.h = h
	def __call__(self, gamma):
		F1 = self.F1
		h = self.h
		return (F1(gamma+h) - F1(gamma-h))/(2*h)

class InverseFunction:
	def __init__(self, f, x):
		# We want to check for monotonicity
		i = 0
		if 0 in x:
			raise ValueError('x cannot contain 0')
		while x[i] == x[i+1]:
			i+=1
		if x[i] > x[i+1]:
			for j in range(i, len(x)-1):
				if x[j] < x[j+1]:
					raise ValueError('No monotonicity')
		elif x[i] < x[i+1]:
			for j in range(i, len(x)-1):
				if x[j] > x[j+1]:
					raise ValueError('No monotonicity')
		self.f = f
		self.x = x
		from Newton import Newton
		from scitools.std import zeros
		g = zeros(len(x))
		a = F(f, x[0])
		b = dFdx(a)
		for i in range(len(x)):
			a.xi = x[i]
			if i == 0:
				gamma0 = x[0]
			else:
				gamma0 = g[i-1]
			gamma, n, F_value = Newton(a, gamma0, b)
			g[i] = gamma
		self.values = g

	def __call__(self, x):
		if x < self.x[0] or x > self.x[-1]:
			raise ValueError('x is outside of valid domain')
		from scitools.std import wrap2callable
		y = self.values
		q = wrap2callable((self.x,y))
		return q(x)

def _test():
#	from InverseFunction import InverseFunction as I
	from scitools.std import log, linspace, plot
	def f(x):
		return log(x)
	x = linspace(1, 5, 101)
	f_inv = InverseFunction(f, x)
	plot(x,f(x),x, f_inv.values,legend=['log(x)', 'inv log(x)'])
	raw_input('Press Enter to quit: ')

if __name__ == '__main__':
	_test()
