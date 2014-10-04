class F:
	def __init__(self, a, w):
		self.a = a
		self.w = w
	def value(self, x):
		from scitools.std import exp, sin
		a = self.a
		w = self.w
		return exp(-a*x)*sin(w*x)

def _test():
	from math import pi
	f = F(a=1.0, w=0.1)
	print f.value(x=pi)
	f.a = 2
	print f.value(pi)

if __name__ == '__main__':
	_test()

'''
python F.py
0.013353835137
0.00057707154012
'''
