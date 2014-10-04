def integrate(f, a, b, n):
    '''an approximation to integration by calculating
    the area of trapezoids n trapezoids
    f is our function
    we integrate from a to b where a < b
    n is the number of trapezoids we use to approximate the integral
    '''
    h = float(b-a)/n
    base = [f(a + i*h) for i in range(n+1)]
    area = [0]*n
    for i in range(n):
        area[i] = 1./2*h*(base[i] + base[i+1])
    return sum(area)


from math import exp, cos, sin, pi, log
f = [lambda x: exp(x), lambda x: cos(x), lambda x: sin(x), lambda x: sin(x)]
F = [lambda x: exp(x), lambda x: sin(x), lambda x: -cos(x), lambda x: -cos(x)]
s = ['exp(x)', 'cos(x)', 'sin(x)', 'sin(x)']
limits = [[0, log(3)], [0, pi], [0, pi], [0, pi/2]]
print '%5s %10s %20s %11s' % ('n', 'function','limits', 'error')
for n in [4,10]:
    for i in range(4):
        exact = F[i](limits[i][1]) - F[i](limits[i][0])
        approx = integrate(f[i], limits[i][0], limits[i][1], n)
        error = abs(exact - approx)
        print '%5d %10s %5f to %5f %11g' % \
                       (n, s[i], limits[i][0], limits[i][1], error)

'''
python int3_f.py
    n   function               limits       error
    4     exp(x) 0.000000 to 1.098612   0.0125566
    4     cos(x) 0.000000 to 3.141593 1.22461e-16
    4     sin(x) 0.000000 to 3.141593    0.103881
    4     sin(x) 0.000000 to 1.570796   0.0128842
   10     exp(x) 0.000000 to 1.098612  0.00201118
   10     cos(x) 0.000000 to 3.141593 2.66117e-16
   10     sin(x) 0.000000 to 3.141593   0.0164765
   10     sin(x) 0.000000 to 1.570796  0.00205701
'''
