Fdegrees = [0]*11
dF = 10 # degrees
for i in range(11):
    Fdegrees[i] = i * dF
Cdegrees = [5.0/9 * (i - 32) for i in Fdegrees]
CdegreesRounded = [(i - 30)/2.0 for i in Fdegrees]
print '    F    C    C Rounded'

for i in range(11):
    F = Fdegrees[i] 
    C1 = Cdegrees[i]
    C2 = CdegreesRounded[i]
    print '%5d %5.1f %5.1f' % (F, C1, C2)

'''
python f2c_approx_table.py
    F    C    C Rounded
    0 -17.8 -15.0
   10 -12.2 -10.0
   20  -6.7  -5.0
   30  -1.1   0.0
   40   4.4   5.0
   50  10.0  10.0
   60  15.6  15.0
   70  21.1  20.0
   80  26.7  25.0
   90  32.2  30.0
  100  37.8  35.0
'''
