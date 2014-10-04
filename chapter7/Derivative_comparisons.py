class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x))/h

from Central import Central

def table(f, x, hlist, dfdx=None):	
	print '%15s %15s %15s' % \
		('h', 'Derivative', 'Central'),
	if dfdx is not None:
		print '%15s' % ('True')
	for h in hlist:
		d = Derivative(f, h)
		c = Central(f, h)
		df_d = d(x)
		df_c = c(x)
		print '%15g %15g %15g' % (h, df_d, df_c),
		if dfdx is not None:
			print '%15f' % (dfdx(x))
		else:
			print ''

from scitools.std import *
f = ['x**2', 'sin(pi*x)**6', 'tanh(10*x)']
df = ['2*x', '6*pi*sin(pi*x)**5*cos(pi*x)', '10*(1-tanh(10*x)**2)']
hlist = [1E-1, 1E-3, 1E-5, 1E-7]
from scitools.StringFunction import StringFunction
x = [0, 0.25]
for a in range(2):
	for b in range(3):
		print 'x = %.2f, f = %s' % (x[a], f[b])
		table(StringFunction(f[b]), x[a], hlist, \
			StringFunction(df[b]))
		print ''

x = linspace(-1,1,500)
for a in f:
	figure()
	plot(x, vectorize(StringFunction(a))(x), title='%s' % a)
raw_input('Press Enter to quit:' )	

'''
python Derivative_comparisons.py
x = 0.00, f = x**2
              h      Derivative         Central            True
            0.1             0.1               0        0.000000
          0.001           0.001               0        0.000000
          1e-05           1e-05               0        0.000000
          1e-07           1e-07               0        0.000000

x = 0.00, f = sin(pi*x)**6
              h      Derivative         Central            True
            0.1      0.00870751               0        0.000000
          0.001      9.6138e-13               0        0.000000
          1e-05     9.61389e-23               0        0.000000
          1e-07     9.61389e-33               0        0.000000

x = 0.00, f = tanh(10*x)
              h      Derivative         Central            True
            0.1         7.61594         7.61594       10.000000
          0.001         9.99967         9.99967       10.000000
          1e-05              10              10       10.000000
          1e-07              10              10       10.000000

x = 0.25, f = x**2
              h      Derivative         Central            True
            0.1             0.6             0.5        0.500000
          0.001           0.501             0.5        0.500000
          1e-05         0.50001             0.5        0.500000
          1e-07             0.5             0.5        0.500000

x = 0.25, f = sin(pi*x)**6
              h      Derivative         Central            True
            0.1         3.75363         2.45804        2.356194
          0.001         2.37101         2.35621        2.356194
          1e-05         2.35634         2.35619        2.356194
          1e-07          2.3562         2.35619        2.356194

x = 0.25, f = tanh(10*x)
              h      Derivative         Central            True
            0.1        0.115636        0.465148        0.265922
          0.001        0.263316        0.265939        0.265922
          1e-05        0.265896        0.265922        0.265922
          1e-07        0.265922        0.265922        0.265922

Press Enter to quit:
'''
