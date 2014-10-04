f2c = lambda x: 5.0/9*(x - 32)
c2f = lambda x: 9.0/5*x + 32
e = 10**-10 # epsilon

print '    C    F    C == f2c(c2f(C))?'
for i in range(0,101,5):
    C = i
    F = c2f(i)
    print '%5.1f %5.1f %15s' % (C, F,bool(abs(C - f2c(F) < e)))

'''
    C    F    C == f2c(c2f(C))?
  0.0  32.0            True
  5.0  41.0            True
 10.0  50.0            True
 15.0  59.0            True
 20.0  68.0            True
 25.0  77.0            True
 30.0  86.0            True
 35.0  95.0            True
 40.0 104.0            True
 45.0 113.0            True
 50.0 122.0            True
 55.0 131.0            True
 60.0 140.0            True
 65.0 149.0            True
 70.0 158.0            True
 75.0 167.0            True
 80.0 176.0            True
 85.0 185.0            True
 90.0 194.0            True
 95.0 203.0            True
100.0 212.0            True
'''
