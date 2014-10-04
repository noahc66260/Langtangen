import sys
from math import *
from sinesum2 import *
usage = '''%s n_values alpha_values T
n_values is a list, alpha_values is a list, T is a number'''\
	% sys.argv[0]
try:
	n_values = eval(sys.argv[1])
	alpha_values = eval(sys.argv[2])
	T = eval(sys.argv[3])
except:
	print usage
	sys.exit(1)
table(n_values, alpha_values, T)

'''
python sinesum3.py '[1,3,5,10,30,100]' '[0.01,0.25,0.49]' 2*pi
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

