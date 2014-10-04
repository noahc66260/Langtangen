import scitools
a = 1/947.0*947
b = 1
print 'Regular comparison'
print 'a == b =', (a == b) 
print 'Using float_eq'
print 'a == b =', scitools.numpyutils.float_eq(a,b)

'''
python compare_float.py
scitools.easyviz backend is gnuplot
Regular comparison
a == b = False
Using float_eq
a == b = True
'''
