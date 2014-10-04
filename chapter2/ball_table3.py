v0 = 1 # m/s
g = 9.81 # m/s**2
n = 11
dt = (2.0*v0/g)/n # s
t = [0]*(n+1)
y = [0]*(n+1)

for i in range(n):
    t[i] = i * dt
    y[i] = v0*t[i] - 0.5*g*t[i]**2

ty1 = [t, y]
ty2 = zip(ty1[0], ty1[-1])

print 'Printing using ty1'
print '    t    y(t)'
for i in range(n):
    print '%5.3f %7.3f' % (t[i], y[i])

print
print 'Printing using ty2'
print '    t    y(t)'
for a,b in ty2:
    print '%5.3f %7.3f' % (a,b)

'''
Printing using ty1
    t    y(t)
0.000   0.000
0.019   0.017
0.037   0.030
0.056   0.040
0.074   0.047
0.093   0.051
0.111   0.051
0.130   0.047
0.148   0.040
0.167   0.030
0.185   0.017

Printing using ty2
    t    y(t)
0.000   0.000
0.019   0.017
0.037   0.030
0.056   0.040
0.074   0.047
0.093   0.051
0.111   0.051
0.130   0.047
0.148   0.040
0.167   0.030
0.185   0.017
0.000   0.000
'''
