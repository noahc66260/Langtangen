Fdegrees = [0]*11
dF = 10 # degrees
for i in range(11):
    Fdegrees[i] = i * dF
Cdegrees = [5.0/9 * (i - 32) for i in Fdegrees]
print '    F    C'
for i in range(11):
    F = Fdegrees[i] 
    C = Cdegrees[i]
    print '%5d %5.1f' % (F, C)

'''
python f2c_table_while.py
    F    C
    0 -17.8
   10 -12.2
   20  -6.7
   30  -1.1
   40   4.4
   50  10.0
   60  15.6
   70  21.1
   80  26.7
   90  32.2
  100  37.8
'''
