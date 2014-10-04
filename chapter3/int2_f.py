def integrate2(f, a, b):
    '''a simplistic approximation to integration to calculating
    the area of two trapezoids.
    f is our function
    we integrate from a to b where a < b
    '''
    base1 = f(a)
    base2 = f((b-a)/2.0)
    base3 = f(b)
    h = (b-a)/2.0
    area1 = 1./2*h*(base1 + base2)
    area2 = 1./2*h*(base2 + base3)
    return area1 + area2

from math import exp, cos, sin, pi, log
f = [lambda x: exp(x), lambda x: cos(x), lambda x: sin(x), lambda x: sin(x)]
F = [lambda x: exp(x), lambda x: sin(x), lambda x: -cos(x), lambda x: -cos(x)]
s = ['exp(x)', 'cos(x)', 'sin(x)', 'sin(x)']
limits = [[0, log(3)], [0, pi], [0, pi], [0, pi/2]]
print '%10s %20s %11s' % ('function','limits', 'error')
for i in range(4):
    exact = F[i](limits[i][1]) - F[i](limits[i][0])
    approx = integrate2(f[i], limits[i][0], limits[i][1])
    error = abs(exact - approx)
    print '%10s %5f to %5f %11g' % (s[i], limits[i][0], limits[i][1], error)

'''
python int2_f.py
  function               limits       error
    exp(x) 0.000000 to 1.098612   0.0500384
    cos(x) 0.000000 to 3.141593 1.14383e-17
    sin(x) 0.000000 to 3.141593    0.429204
    sin(x) 0.000000 to 1.570796   0.0519406
'''
