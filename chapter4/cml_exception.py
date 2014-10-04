import sys
try:
	C = float(sys.argv[1])
except IndexError:
	print 'C must be provided as command-line argument'
	sys.exit(1)
except ValueError:
	print 'C must be provided as a real number'
	sys.exit(1)
F = 9.0/5*C + 32
print '%.2f degrees C = %.2f degrees F' % (C, F)

