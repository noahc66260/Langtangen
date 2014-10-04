from scitools.std import *

def Secant(f, x0, x1, epsilon = 1e-10, N=100, store=False):
	f_value0 = f(x0)
	f_value1 = f(x1)
	if store:
		info = [(x1, f_value1)]

	n = 1
	xnm1 = x1
	xnm2 = x0
	f_value_xnm1 = f(xnm1)
	f_value_xnm2 = f(xnm2)
	while abs(f_value_xnm1) > epsilon and n < N:
		xn = xnm1 - float(f_value_xnm1)*(xnm1 - xnm2) \
				/ (f_value_xnm1 - f_value_xnm2)
		xnm2 = xnm1
		xnm1 = xn
		f_value_xnm1 = f(xnm1)
		f_value_xnm2 = f(xnm2)
		if store:
			info.append((xnm1, f_value_xnm1))
		n += 1

	x = xnm1
	if store:
		return x, info
	else:
		return x


def _test1():
	f = lambda x: x**5 - sin(x)
	x0 = 1
	x1 = 2
	N = 100
	epsilon = 1e-10
	x, info = Secant(f, x0, x1,epsilon,N, True)
	
	info = transpose(info)
	x_values = info[0]
	f_values = info[1]
	
	
	figure()
	plot(x_values,
		xlabel='Iteration Number',
		ylabel='x_i',
		title='Secant method for f = x**5 - sin(x), '\
			'Iteration number vs. x_i')
	
	figure()
	semilogy(f_values,
		xlabel='Iteration Number',
		ylabel='f(x_i)',
		axes=[0, len(f_values), -1e-1,1e-1],
		title='Secant method for f = x**5 - sin(x), '\
			'Iteration number vs. f(x_i)')
	
	raw_input('Press Enter to quit: ')

def _test2():
	from scitools.std import sin
	f = lambda x: sin(x)
	x0 = 1
	x1 = 2
	x, info = Secant(f, x0, x1,1e-10,100, True)
	x_values = transpose(info)[0]
	f_values = transpose(info)[1]
	for i in range(len(x_values)):
		print '%10f %10f' % (x_values[i], f_values[i])
	
	
if __name__ == '__main__':
	_test1()	
	_test2()
