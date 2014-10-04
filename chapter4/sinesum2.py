from math import sin, pi

def S(t,n,T):
    sum = 0
    for i in range(1,n+1):
        sum += 1./(2*i-1)*sin(2*(2*i-1)*pi*t/T)
    return sum*4/pi

def f(t, T):
    if 0 < t < T/2.0:
        x = 1
    elif t == T/2.0:
        x = 0
    elif T/2.0 < t < T:
        x = -1
    return x

def table(n_values, alpha_values, T):
	print '    n    alpha    approximation     error'
	for i in n_values:
	    for j in alpha_values:
		approx = S(T*j, i, T)
		error = abs(f(T*j, T) - approx)
		print '%5d %8.2f %16f %9.2g' % (i,j,approx,error)
	

if __name__ == '__main__':
	n = [1,3,5,10,30,100]
	alpha = [0.01, 0.25, 0.49]
	T = 2*pi
	table(n, alpha, T)

'''
python sinesum2.py
    n    alpha    approximation     error
    1     0.01         0.079947      0.92
    1     0.25         1.273240      0.27
    1     0.49         0.079947      0.92
    3     0.01         0.238165      0.76
    3     0.25         1.103474       0.1
    3     0.49         0.238165      0.76
    5     0.01         0.391415      0.61
    5     0.25         1.063054     0.063
    5     0.49         0.391415      0.61
   10     0.01         0.733203      0.27
   10     0.25         0.968248     0.032
   10     0.49         0.733203      0.27
   30     0.01         1.144816      0.14
   30     0.25         0.989393     0.011
   30     0.49         1.144816      0.14
  100     0.01         0.949906      0.05
  100     0.25         0.996817    0.0032
  100     0.49         0.949906      0.05
'''
