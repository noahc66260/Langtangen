def C2F(C):
	'''
	Converts from Celsius to Fahrenheit
	'''
	return 9.0/5*C + 32

def F2C(F):
	'''
	Converts from Fahrenheit to Celius
	'''
	return (F - 32.0)*5.0/9

def C2K(C):
	'''
	Converts from Celius to Kelvin
	'''
	return C + 273.15

def K2C(K):
	'''
	Converts from Kelvin to Celsius
	'''
	return K - 273.15

def F2K(F):
	'''
	Converts from Fahrenheit to Kelvin
	'''
	return (F - 32.0)*5.0/9 + 273.15

def K2F(K):
	'''
	Converts from Kelvin to Fahrenheit
	'''
	return (K - 273.15)*9.0/5 + 32


if __name__ == '__main__':
	import sys
	_usage = '%s x scale\nx is a real number, scale is F, C, or K' \
		% sys.argv[0]
	try:
		x = eval(sys.argv[1])
		scale = sys.argv[2]
	except:
		print _usage
		sys.exit(1)
	if scale == 'C':
		print '%.2f %s %.2f %s' % (C2F(x), 'F', C2K(x), 'K')
	elif scale == 'F':
		print '%.2f %s %.2f %s' % (F2C(x), 'C', F2K(x), 'K')
	elif scale == 'K':
		print '%.2f %s %.2f %s' % (K2F(x), 'F', K2C(x), 'C')
	else:
		raise ValueError('scale must be F, C, or K')

'''
python convert_temp2.py 21.3 C
70.34 F 294.45 K
'''
	
