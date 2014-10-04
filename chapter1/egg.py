smallEggMass = 47 # g
largeEggMass = 67 # g
eggDensity = 1.038 # g / cm**-3
specificHeatCapacity = 3.7 # J * g**-1 * K**-1
thermalConductivity = 5.4 * 10**-3 # W * cm**-1 * K**-1
T_w = 100 # C, temperature of boiling water
T_o_1 = 4 # C, initial temperature of egg from refrigerator
T_o_2 = 20 # C, initial temperature of egg, room temperature
T_y = 70 # C

from math import pi, log

t1 = (smallEggMass**(2./3) * specificHeatCapacity * eggDensity**(1./3)) \
    / (thermalConductivity * pi**2 * (4*pi/3)**(2./3)) \
    * log(0.76 * (float(T_o_1) - T_w)/(T_y - T_w))
t2 = (smallEggMass**(2./3) * specificHeatCapacity * eggDensity**(1./3)) \
    / (thermalConductivity * pi**2 * (4*pi/3)**(2./3)) \
    * log(0.76 * (float(T_o_2) - T_w)/(T_y - T_w))
t3 = (largeEggMass**(2./3) * specificHeatCapacity * eggDensity**(1./3)) \
    / (thermalConductivity * pi**2 * (4*pi/3)**(2./3)) \
    * log(0.76 * (float(T_o_1) - T_w)/(T_y - T_w))
t4 = (largeEggMass**(2./3) * specificHeatCapacity * eggDensity**(1./3)) \
    / (thermalConductivity * pi**2 * (4*pi/3)**(2./3)) \
    * log(0.76 * (float(T_o_2) - T_w)/(T_y - T_w))

print """We have the following cooking times
%.2f seconds for a small egg from the refrigerator
%.2f seconds for a small egg at room temperature
%.2f seconds for a large egg from the refrigerator
%.2f seconds for a large egg at room temperature""" % (t1, t2, t3, t4)

'''
We have the following cooking times
313.09 seconds for a small egg from the refrigerator
248.86 seconds for a small egg at room temperature
396.58 seconds for a large egg from the refrigerator
315.22 seconds for a large egg at room temperature
'''
