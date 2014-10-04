import sys
from scitools.StringFunction import StringFunction
from Newton import Newton
from Secant import Secant
from bisection import bisection_evolution
from scitools.std import *

usage = 'f(x) f\'(x) a b x0 x1'
try:
	f  = StringFunction(sys.argv[1])
	df = StringFunction(sys.argv[2])
	a  = float(eval(sys.argv[3]))
	b  = float(eval(sys.argv[4]))
	x0 = float(eval(sys.argv[5]))
	x1 = float(eval(sys.argv[6]))
except:
	print usage
	sys.exit(1)

def printRootConvergence(x_values, f_values, method_name=None):
	if method_name is not None:
		print method_name
	print '%5s %15s %15s' % ('n', 'root', 'f(x)')
	for i in range(len(f_values)):
		print '%5d %15.10f %15.10f' % (i+1, x_values[i], f_values[i])
	
	

N = 100
epsilon = 1e-10

figure()
x, item = Newton(f, x0, df, epsilon, N, True)
x_values = transpose(item)[0]
f_values = transpose(item)[1]
printRootConvergence(x_values, f_values, 'Newton\'s Method')
semilogy(abs(f_values),'-o-',
	xlabel='Iteration Number',
	ylabel='abs(f(x_i))',
	title='Newton''s Method for %s = 0' % sys.argv[1])
raw_input('Press Enter to continue: ')

figure()
x, item = Secant(f, x0, x1, epsilon, N, True)
x_values = transpose(item)[0]
f_values = transpose(item)[1]
printRootConvergence(x_values, f_values, 'Secant Method')
semilogy(abs(f_values),'-o-',
	xlabel='Iteration Number',
	ylabel='abs(f(x_i))',
	title='Secant Method for %s = 0' % sys.argv[1])
raw_input('Press Enter to continue: ')

figure()
result = bisection_evolution(f, a, b, epsilon)
x_values = transpose(result)[1]
f_values = array([f(i) for i in x_values])
printRootConvergence(x_values, f_values, 'Bisection Method')
semilogy(abs(f_values), '-o-',
	xlabel='Iteration Number',
	ylabel='abs(f(x_i))',
	title='Bisection Method for %s = 0' % sys.argv[1])

raw_input('Press Enter to quit: ')

'''
python root_finder_examples.py 'sin(x)' 'cos(x)' -2 1 1 1.1
Newton's Method
    n            root            f(x)
    1    1.0000000000    0.8414709848
    2   -0.5574077247   -0.5289880971
    3    0.0659364519    0.0658886846
    4   -0.0000957219   -0.0000957219
    5    0.0000000000    0.0000000000
Press Enter to continue: 
Secant Method
    n            root            f(x)
    1    1.1000000000    0.8912073601
    2   -0.6918623050   -0.6379723729
    3    0.0557009944    0.0556721959
    4   -0.0042987408   -0.0042987275
    5    0.0000020520    0.0000020520
    6   -0.0000000000   -0.0000000000
Press Enter to continue: 
Bisection Method
    n            root            f(x)
    1   -0.5000000000   -0.4794255386
    2    0.2500000000    0.2474039593
    3   -0.1250000000   -0.1246747334
    4    0.0625000000    0.0624593178
    5   -0.0312500000   -0.0312449140
    6    0.0156250000    0.0156243642
    7   -0.0078125000   -0.0078124205
    8    0.0039062500    0.0039062401
    9   -0.0019531250   -0.0019531238
   10    0.0009765625    0.0009765623
   11   -0.0004882812   -0.0004882812
   12    0.0002441406    0.0002441406
   13   -0.0001220703   -0.0001220703
   14    0.0000610352    0.0000610352
   15   -0.0000305176   -0.0000305176
   16    0.0000152588    0.0000152588
   17   -0.0000076294   -0.0000076294
   18    0.0000038147    0.0000038147
   19   -0.0000019073   -0.0000019073
   20    0.0000009537    0.0000009537
   21   -0.0000004768   -0.0000004768
   22    0.0000002384    0.0000002384
   23   -0.0000001192   -0.0000001192
   24    0.0000000596    0.0000000596
   25   -0.0000000298   -0.0000000298
   26    0.0000000149    0.0000000149
   27   -0.0000000075   -0.0000000075
   28    0.0000000037    0.0000000037
   29   -0.0000000019   -0.0000000019
   30    0.0000000009    0.0000000009
   31   -0.0000000005   -0.0000000005
   32    0.0000000002    0.0000000002
   33   -0.0000000001   -0.0000000001
   34    0.0000000001    0.0000000001
   35   -0.0000000000   -0.0000000000
Press Enter to quit: 
'''


