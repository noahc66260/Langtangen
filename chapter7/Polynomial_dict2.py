class Polynomial:
	def __init__(self, coeff):
		from numpy import ndarray
		if isinstance(coeff, (ndarray, list, tuple)):
			self.coeff = {}
			for i, c in enumerate(coeff[:]):
				 if c != 0:
					self.coeff[i] = c
		elif isinstance(coeff, dict):
			self.coeff = coeff.copy()
		else:
			raise ValueError('Argument must be list or dict')

	def __add__(self, other):
		from scitools.std import copy
		result = self.coeff.copy()
		for i in other.coeff:
			if i in result:
				result[i] += other.coeff[i]
			else:
				result[i] = other.coeff[i]
			if result[i] == 0:
				del result[i]
		return Polynomial(result)

	def __str__(self):
		s = ""
		for i in sorted(self.coeff):
			s += '+ %dx**%d ' % (self.coeff[i], i)	
		s = s[2:-1] # get rid of leading '+ ', trailing ' '
		s = s.replace('+ -', '- ')
		s = s.replace('1x', 'x')
		s = s.replace('**1 ', ' ') # x**1 --> x
		return s

	def __mul__(self, other):
		product = {}
		for i in self.coeff:
			for j in other.coeff:
				if (i+j) in product:
					product[i+j] += \
						self.coeff[i]*other.coeff[j]
				else:
					product[i+j] = \
						self.coeff[i]*other.coeff[j]
		return Polynomial(product)

def _test():
	x1 = {1: 1, 100: -3}
	x2 = {20: 1, 1: -1, 100: 4}
	p1 = Polynomial(x1)
	p2 = Polynomial(x2)
	p3 = p1 + p2
	print p1,'+ (',p2,') =', p3
	p4 = p1 * p2
	print '(%s)*(%s) = %s' % (p1, p2, p4)

if __name__ == '__main__':
	_test()	

'''
python Polynomial_dict2.py
x - 3x**100 + ( -x + x**20 + 4x**100 ) = x**20 + x**100
(x - 3x**100)*(-x + x**20 + 4x**100) = -x**2 + x**21 + 7x**101 - 3x**120 - 12x**200
'''
