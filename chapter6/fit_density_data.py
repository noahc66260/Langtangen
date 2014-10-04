import sys
from scitools.std import *
usage = '%s *.dat' % sys.argv[0]

try: 
	filename = sys.argv[1]
except:
	print usage
	sys.exit(1)

infile = open(filename, 'r')
temp = [] # in deg C
density = [] # in kg/m**3
for line in infile:
	if line[0] == '#' or line.strip() == '':
		continue
	else:
		words = line.split()
		temp.append(float(words[0]))
		density.append(float(words[1]))
infile.close()
coeff1 = polyfit(temp, density,1)
p1 = poly1d(coeff1)
coeff2 = polyfit(temp, density,2)
p2 = poly1d(coeff2)
density_fitted_1 = p1(temp)
density_fitted_2 = p2(temp)

plot(temp, density,
	temp, density_fitted_1,
	temp, density_fitted_2,
	xlabel='Temperature (C)', ylabel='Density (kg/m**3)',
	legend=['Data', 'Degree-1 Polynomial Fit', 'Degree-2 Polynomial Fit'])
raw_input('Press Enter to quit: ')

