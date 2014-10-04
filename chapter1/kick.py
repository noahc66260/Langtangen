from math import pi
g = 9.81 # m/s**2, acceleration due to gravity
rho = 1.2 # kg/m**3, density of air
a = 11 # cm, the radius of the area of the football normal to the
       # velocity vector
A = pi * (a/100.)**2 # m**2 cross section of football
m = .43 # kg, mass of football
C_D = 0.2 # drag coefficient
v1 = 120 # km/h, hard kick
v2 = 10  # km/h, soft kick

F_d_1 = 1./2 * C_D * rho * A * (v1*1000./3600) # in kg * m/s**2
F_d_2 = 1./2 * C_D * rho * A * (v2*1000./3600) # in kg * m/s**2
F_g = m * g # kg * m/s**2

print """Drag force at v = %.1g km/h = %.1g N
Drag force at v = %.1g km/h = %.1g N
Gravatational force at either velocity = %.1g N
Ratio of drag force to gravity force for hard kick = %.g
Ratio of drag force to gravity force for soft kick = %.g""" \
% (v1, F_d_1, v2, F_d_2, F_g, F_d_1 / F_g, F_d_2 / F_g)

'''
python kick.py
Drag force at v = 1e+02 km/h = 0.2 N
Drag force at v = 1e+01 km/h = 0.01 N
Gravatational force at either velocity = 4 N
Ratio of drag force to gravity force for hard kick = 0.04
Ratio of drag force to gravity force for soft kick = 0.003
'''
