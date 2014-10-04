filename = 'stars.list'
infile = open(filename, 'r')
exec(infile.read()) # now data should be a variable

star = {}
for s in data:
	star[s[0]] = s[-1]

for entry in sorted(star):
	print '%s has luminosity of %f' % (entry, star[entry])

'''
python stars_data_dict1.py
Alpha Centauri A has luminosity of 1.560000
Alpha Centauri B has luminosity of 0.450000
Alpha Centauri C has luminosity of 0.000060
BD +36 degrees 2147 has luminosity of 0.006000
Barnard's Star has luminosity of 0.000500
Luyten 726-8 A has luminosity of 0.000060
Luyten 726-8 B has luminosity of 0.000040
Ross 154 has luminosity of 0.000500
Sirius A has luminosity of 23.600000
Sirius B has luminosity of 0.003000
Wolf 359 has luminosity of 0.000020
'''
