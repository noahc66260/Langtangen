n = 20
x = [float(i)/n for i in range(1,n+1)]
print '    x    arcsin(x)    sin(arcsin(x)) == x'
from math import sin, asin
for i in x:
    print '%5.3f %12.3f %21s' % (i, asin(i), sin(asin(i)) == i)

'''
    x    arcsin(x)    sin(arcsin(x)) == x
0.050        0.050                  True
0.100        0.100                  True
0.150        0.151                  True
0.200        0.201                  True
0.250        0.253                  True
0.300        0.305                  True
0.350        0.358                  True
0.400        0.412                  True
0.450        0.467                  True
0.500        0.524                  True
0.550        0.582                  True
0.600        0.644                  True
0.650        0.708                  True
0.700        0.775                  True
0.750        0.848                  True
0.800        0.927                  True
0.850        1.016                  True
0.900        1.120                  True
0.950        1.253                  True
1.000        1.571                  True
'''
