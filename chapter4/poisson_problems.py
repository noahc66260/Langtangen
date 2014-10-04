import argparse
from poisson_distribution import *
from math import *
import sys
usage = '%s -x %s -t %s -nu %s' % (sys.argv[0], 'random_variable', 'time', 'number_of_occurences_in_interval')
parser = argparse.ArgumentParser()
parser.add_argument('--x', '-x', type=int, help='random variable')
parser.add_argument('--t', '-t',type=float, help='time')
parser.add_argument('--nu', '-nu', type=float, help='average number of occurrences per unit time')
try:
	args = parser.parse_args()
except:
	print usage
p = Poisson(args.x, args.t, args.nu)
print 'The probability of %d occurrences for t = %.2f and nu = %.2f is %f' % (args.x, args.t, args.nu, p)

'''
# for problem 1
python poisson_problems.py --x 0 --t 2 --nu 5
The probability of 0 occurrences for t = 2.00 and nu = 5.00 is 0.000045

python poisson_problems.py --x 2 --t .33 --nu 5
The probability of 2 occurrences for t = 0.33 and nu = 5.00 is 0.261428

# I'm skipping the computation for 2 and 3 since it's just plugging in numbers
'''
