def L3(x, n=None, epsilon=None, return_n=False):
	if n is None and epsilon is None:
		print 'You must specifiy either n or epsilon but not neither'
	elif n is not None and epsilon is not None:
		print 'You cannot specify both n and epsilon'
	elif n is not None and epsilon is None:
		s = 0
		for i in range(1, n+1):
			s += (1.0/i)*(x/(1.0+x))**i
		value_of_sum = s
		return value_of_sum
	elif n is None and epsilon is not None and return_n == False:
		x = float(x)
		i = 1
		term = (1.0/i)*(x/(1+x))**i
		s = term
		while abs(term) > epsilon:
			i += 1
			term = (1.0/i)*(x/(1+x))**i
			s += term
		return s	
	elif n is None and epsilon is not None and return_n == True:
		x = float(x)
		i = 1
		term = (1.0/i)*(x/(1+x))**i
		s = term
		while abs(term) > epsilon:
			i += 1
			term = (1.0/i)*(x/(1+x))**i
			s += term
		return s, i
	else:
		print 'An error occured'


def table(x):
    from math import log
    print '\nx=%g, ln(1+x)=%g' % (x, log(1+x))
    for n in [1, 2, 10, 100, 500]:
        value = L3(x, n=n)
        print 'n=%-4d %-10g' % (n, value)
    
table(10)
table(100)
table(1000)

print '\n\n'
from math import log
x = 10
print 'x =', x
for k in range(4, 14, 2):
    epsilon = 10**(-k)
    approx, n = L3(x, epsilon=epsilon, return_n = True)
    exact = log(1+x)
    exact_error = exact - approx
    print 'epsilon: %5.0e, exact error: %8.2e, n=%d' % \
          (epsilon, exact_error, n)


'''
python L3_flexible.py

x=10, ln(1+x)=2.3979
n=1    0.909091  
n=2    1.32231   
n=10   2.17907   
n=100  2.39789   
n=500  2.3979    

x=100, ln(1+x)=4.61512
n=1    0.990099  
n=2    1.48025   
n=10   2.83213   
n=100  4.39574   
n=500  4.61395   

x=1000, ln(1+x)=6.90875
n=1    0.999001  
n=2    1.498     
n=10   2.919     
n=100  5.08989   
n=500  6.34928   



x = 10
epsilon: 1e-04, exact error: 8.18e-04, n=55
epsilon: 1e-06, exact error: 9.02e-06, n=97
epsilon: 1e-08, exact error: 8.70e-08, n=142
epsilon: 1e-10, exact error: 9.20e-10, n=187
epsilon: 1e-12, exact error: 9.31e-12, n=233
'''
