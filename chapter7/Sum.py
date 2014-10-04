class Sum:
	def __init__(self, f, M, N):
		self.f = f
		self.M = M
		self.N = N

	def __call__(self, x):
		sum = 0
		N = self.N
		M = self.M
		f = self.f
		for k in range(M, N+1):
			sum += f(k,x)
		self.first_neglected_term = f(N+1,x)
		# it appears we get problems storing neglected_term
		# due to underflow
		return sum

def _test():
	def term (k,x): return (-x)**k
	S = Sum(term, M=0, N=100)
	x = 0.5
	print S(x)
	# Print the value of the first neglected term from the last S(x) comp.
	print S.first_neglected_term

	from math import sin, pi, exp
	print 'We compute the approximation to sin(x)'
	print '%10s %10s %15s %25s' % \
		 ('x', 'terms', 'error', 'first neglected term')
	x = [pi, 30*pi]
	N = [5,10,20]
	for i in N:
		for j in x:
			def taylor_sin_term(k,x):
				from math import factorial
				return (-1)**k / float(factorial(2*k+1)) * \
					x**(2*k+1)
			S = Sum(taylor_sin_term, M=0, N=i)
			approx = S(j)
			error = sin(j) - approx
			print '%10f %10d %15g %25g' % \
				(j, i, error, S.first_neglected_term)

	print ''
	print 'We compute the approximation to exp(x)'
	print '%10s %10s %15s %25s' % \
		 ('x', 'terms', 'error', 'first neglected term')
	x = [1,3,5]
	N = [5,10,20]
	for i in N:
		for j in x:
			def taylor_exp(k,x):
				from math import factorial
				return x**k / float(factorial(k))
			S = Sum(taylor_exp, M=0, N=i)
			approx = S(j)
			error = exp(j) - approx
			print '%10d %10d %15g %25g' % \
				(j, i, error, S.first_neglected_term)
	

if __name__ == '__main__':
	_test()	


'''
python Sum.py
0.666666666667
-3.94430452611e-31
We compute the approximation to sin(x)
         x      terms           error      first neglected term
  3.141593          5      0.00044516               0.000466303
 94.247780          5     1.28961e+14               7.43437e+15
  3.141593         10    -1.03481e-11              -1.05185e-11
 94.247780         10    -5.38416e+21              -9.90242e+22
  3.141593         20    -2.24169e-16              -3.94728e-32
 94.247780         20    -2.21848e+31              -1.29572e+32

We compute the approximation to exp(x)
         x      terms           error      first neglected term
         1          5      0.00161516                0.00138889
         3          5         1.68554                    1.0125
         5          5         56.9965                   21.7014
         1         10     2.73127e-08               2.50521e-08
         3         10      0.00587174                0.00443791
         5         10         2.03256                   1.22325
         1         20    -4.44089e-16               1.95729e-20
         3         20     2.36824e-10                2.0474e-10
         5         20     1.20352e-05               9.33311e-06
'''
