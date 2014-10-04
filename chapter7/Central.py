class Central:
	def __init__(self, f, h=1E-6):
		self.f = f
		self.h = h
	def __call__(self, x):
		h = self.h
		f = self.f
		df = (f(x+h) - f(x-h))/float(2*h)
		return df

def _test():
	from scitools.std import log
	h = [0.5, 0.1, 1E-3, 1E-5, 1E-7, 1E-9, 1E-11]
	x = 10
	print 'for function log(x), x=10'
	print '%10s %10s %10s' % ('h', 'df_approx', 'df_actual')
	for i in h:
		df = Central(log, i)
		df_approx = df(x)
		df_actual = 1./x
		print '%10g %10g %10.1f' % (i, df_approx, df_actual)

if __name__ == '__main__':
	_test()

'''
python Central.py
for function log(x), x=10
         h  df_approx  df_actual
       0.5   0.100083        0.1
       0.1   0.100003        0.1
     0.001        0.1        0.1
     1e-05        0.1        0.1
     1e-07        0.1        0.1
     1e-09        0.1        0.1
     1e-11  0.0999867        0.1
'''
