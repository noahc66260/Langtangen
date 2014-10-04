class F:
	def __init__(self, a, w):
		self.a = a
		self.w = w
	def value(self, x):
		from scitools.std import exp, sin
		a = self.a
		w = self.w
		return exp(-a*x)*sin(w*x)
	def __call__(self, x):
		return self.value(x)
	def __str__(self):
		return 'exp(-a*x)*sin(w*x)'

def _test():
	from math import pi
	f = F(a=1.0, w=0.1)
	print f(pi)
	f.a = 2
	print f(pi)
	print f

if __name__ == '__main__':
	_test()

'''
python F2.py
0.013353835137
0.00057707154012
exp(-a*x)*sin(w*x)
'''
