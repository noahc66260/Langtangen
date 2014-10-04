class Polynomial:
	def __init__(self, coefficients):
		self.coeff = coefficients
	
	def __call__(self, x):
		return sum([c*x**i for i, c in enumerate(self.coeff)])
	
	def __add__(self, other):
		maxlength = max(len(self), len(other))
		# Extend both lists with zeros to this maxlength
		self.coeff += [0]*(maxlength - len(self.coeff))
		other.coeff += [0]*(maxlength - len(other.coeff))
		result_coeff = self.coeff
		for i in range(maxlength):
			result_coeff[i] += other.coeff[i]
		return Polynomial(result_coeff)

	def __len__(self):
		return len(self.coeff)

def _test():
	x = [0,1,0,1]
	y = [1,0,1]
	p1 = Polynomial(x)
	p2 = Polynomial(y)
	ans = p1 + p2
	print 'Our polynomial is \sum x**i for i = 0,1,2,3'
	print 'Thus, p(2) should equal 1 + 2 + 4 + 8 = 2**4 - 1 = 15'
	print 'And our answer is', ans(2)

if __name__ == '__main__':
	_test()

'''
python Polynomial_error.py
Our polynomial is \sum x**i for i = 0,1,2,3
Thus, p(2) should equal 1 + 2 + 4 + 8 = 2**4 - 1 = 15
And our answer is 15
'''
