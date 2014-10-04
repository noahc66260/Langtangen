def diff(f,x,h=1E-6):
    return (f(x+h) - f(x-h)) / (2.0*h)

from math import exp, sin, cos, pi, log

f1 = lambda x: exp(x)
f2 = lambda x: exp(-2*x**2)
f3 = lambda x: cos(x)
f4 = lambda x: log(x)
df1 = lambda x: exp(x)
df2 = lambda x: -4*x*exp(-2*x**2)
df3 = lambda x: -sin(x)
df4 = lambda x: 1.0/x

print '          f(x)    error of approx'
s1 = 'exp(x)'
s2 = 'exp(-2x**2)'
s3 = 'cos(x)'
s4 = 'log(x)'
s = [s1, s2, s3, s4]
f = [f1, f2, f3, f4]
df = [df1, df2, df3, df4]
x = [0, 0, 2*pi, 1]
h = 0.01

for i in range(4):
    error = abs(df[i](x[i]) - diff(f[i], x[i], h))
    print '%15s %15g' % (s[i], error)

'''
python diff_f.py
          f(x)    error of approx
         exp(x)     1.66667e-05
    exp(-2x**2)               0
         cos(x)     2.44921e-16
         log(x)     3.33353e-05
'''
