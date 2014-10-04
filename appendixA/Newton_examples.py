from Newton import *
from scitools.std import *

f = [lambda x: sin(x), 
	lambda x: sin(x) - x,
	lambda x: sin(x) - x**5,
	lambda x: x**4 * sin(x),
	lambda x: x**4,
	lambda x: x**10,
	lambda x: tanh(x) - x**10]

df = [lambda x: cos(x),
	lambda x: cos(x) - 1,
	lambda x: cos(x) - 5*x**4,
	lambda x: 4*x**3 * sin(x) + x**4 * cos(x),
	lambda x: 4*x**3,
	lambda x: 10*x**9,
	lambda x: 1./cosh(x)**2 - 10*x**9]

x0 = 0.1
data = [[]]*len(f)
for i in range(len(f)):
	x, info = Newton(f=f[i], x=x0, dfdx=df[i], \
		epsilon=1.0E-12, N=100, store=True)
	for j in range(len(info)):
		data[i] = append(data[i], info[j][-1])

for i in range(len(f)):
	figure()
	plot(range(len(data[i])), data[i])

raw_input('Press Enter to quit: ')
