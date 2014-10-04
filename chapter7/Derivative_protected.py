class Derivative:
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)

    def __call__(self, x):
        f, h = self._f, self._h      # make short forms
        return (f(x+h) - f(x))/h

    def get_precision(self):
        return self._h

    def set_precision(self, h):
        self._h = h

def _test():
	from scitools.std import log
	x = 1
	k = range(1,46,4)
	print 'Approx error for derivative, relative error'
	print '%10s %20s' % ('precision', 'relative error (%)')
	d = Derivative(log)
	for i in k:
		d.set_precision(2**-i)
		dx = 1.
		error = abs((1.-d(x))/dx*100) # this is in percent
		print '2**-%-6d %20f' % \
			(i, error)

if __name__ == '__main__':
	_test()

'''
Approx error for derivative, relative error
 precision   relative error (%)
2**-1                 18.906978
2**-5                  1.530692
2**-9                  0.097529
2**-13                 0.006103
2**-17                 0.000381
2**-21                 0.000024
2**-25                 0.000001
2**-29                 0.000000
2**-33                 0.000000
2**-37                 0.000000
2**-41                 0.000000
2**-45                 0.000000
'''
