F = [i*10 for i in range(11)]
C = [(i - 32)*5.0/9 for i in F]
C_approx = [(i-30)/2.0 for i in F]
conversion = zip(F, C, C_approx)

print '    F      C     C_approx'
for a,b,c in conversion:
    print '%5.0f %6.2f %12.1f' % (a,b,c)

'''
python f2c_approx_lists.py
    F      C     C_approx
    0 -17.78        -15.0
   10 -12.22        -10.0
   20  -6.67         -5.0
   30  -1.11          0.0
   40   4.44          5.0
   50  10.00         10.0
   60  15.56         15.0
   70  21.11         20.0
   80  26.67         25.0
   90  32.22         30.0
  100  37.78         35.0
'''
