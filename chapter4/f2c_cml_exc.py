import sys
try:
	F = eval(sys.argv[1])
except:
	print 'Fahrenheit degrees must be supplied to the command line'
	sys.exit(1)
C = (F - 32.0)*5.0/9
print '%.1f F = %.1f C' % (F, C)
