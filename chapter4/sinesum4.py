import argparse
from sinesum2 import *
from math import *
parser = argparse.ArgumentParser()
parser.add_argument('--n', '-n', type=list, default=[1,10,100], help='number of terms')
parser.add_argument('--alpha', '-alpha',type=list,default=[0.01,0.25,0.49], help='alpha values')
parser.add_argument('--T', '-T', type=float, default=2*pi)

args = parser.parse_args()
table(args.n, args.alpha, args.T)
