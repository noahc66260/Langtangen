from Newton import *
from scitools.std import *

f = lambda x: x**6 * sin(pi*x)
df = lambda x: 6*x**5 * sin(pi*x) + x**6 * pi * cos(pi*x)

x0 = sort([-2.6, -1.2, 1.5, 1.7, 0.6])
for i in x0:
	x, info = Newton(f, i, df, epsilon=1e-13, N = 100, store=True)
	# we assume convergence for this exercise
	info = transpose(info)
	x_values = info[0]
	f_values = info[1]
	figure()
	plot(range(len(x_values)), x_values,
		xlabel='Iteration Number',
		ylabel='x-value',
		title='Newton''s Method f = x**6 * sin(pi*x), x0 = %.1f' % i)
	figure()
	plot(range(len(f_values)), f_values,
		xlabel='Iteration Number',
		ylabel='f(x_i)',
		title='Newton''s Method f = x**6 * sin(pi*x), x0 = %.1f' % i)
raw_input('Press Enter to quit: ')
