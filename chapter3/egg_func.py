def egg(M, To = 20, Ty = 70):
    '''Returns the time required for the center of the yolk of an
    egg to reach a specified temperature

    M = mass of egg in grams
    To = original temperature of the gg
    Ty = internal temperature we aim to reach inside the egg
    Tw = temperature of water in which the egg cooks
    rho = density of the egg
    c = specific heat capacity of the egg
    K = thermal conductivity of the egg
    '''
    from math import log, pi
    rho = 1.038 # g cm**-3
    c = 3.7 # J g**-1 K**-1
    K = 5.4 * 10**-3 # W cm**-1 K**-1
    Tw = 100 # degrees C
    
    t = M**(2./3)*c*rho**(1./3) / (K * pi**2 *(4.*pi/3)**(2./3)) \
        * log(0.76*float(To - Tw)/(Ty - Tw))
    return t

mass = [47, 67]
temperature = [4, 25]
print ' Mass (grams)   Temperature (C)   Time to Cook (s)'
for i in mass:
    for j in temperature:
        t = egg(M = i, To = j)
        print '%8d %15d %17d' % (i,j,t)

'''
python egg_func.py
 Mass (grams)   Temperature (C)   Time to Cook (s)
      47               4               313
      47              25               226
      67               4               396
      67              25               286
'''
