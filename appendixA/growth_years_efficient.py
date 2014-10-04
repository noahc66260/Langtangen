from scitools.std import *
x0 = 100                      # initial amount
p = 5                         # interest rate
N = 4                         # number of years

xnm1 = x0
# Compute solution
n = 0
while n < N:
	xn = xnm1 + (p/100.0)*xnm1
	xnm1 = xn
	n += 1
print 'After %d years our pricipal of %.2f with %.1f%% interest' % (N, x0, p),
print 'has grown to %.2f' % xn

'''
python growth*
After 4 years our pricipal of 100.00 with 5.0% interest has grown to 121.55
'''
