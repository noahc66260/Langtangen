def cossum(x, n):
	'''
	Calculates the power series of the cosine function
	using the first n terms
	'''
	term = 1
	s = term 
	for i in range(1,n):
		term = -term * x**2 / (2*i*(2*i-1))
		s += term
	return s

from math import pi, cos
x = [4*pi + 2*pi*i for i in range(4)]
n = [5,25,50,100,200]
print '%10s %10s %10s %10s %10s %10s' % ('x', '5', '25', '50', '100', '200')
for i in x:
	print '%10.4f' % (i),
	for j in n:
		print '%10.2e' % (cos(i) - cossum(i,j)),
	print ""

'''
python cossum.py
         x          5         25         50        100        200
   12.5664  -1.09e+04  -2.82e-10   1.74e-12   1.74e-12   1.74e-12 
   18.8496  -3.38e+05  -1.69e-01   7.12e-11   7.12e-11   7.12e-11 
   25.1327  -3.61e+06  -2.72e+05  -4.87e-07  -4.87e-07  -4.87e-07 
   31.4159  -2.22e+07  -1.72e+10   1.65e-04   1.65e-04   1.65e-04 
'''
