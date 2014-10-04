filename = 'stars.list'
infile = open(filename, 'r')
exec(infile.read()) # now data should be a variable

stars = {}
for s in data:
	stars[s[0]] = {'distance': float(s[1]),
			'apparent brightness': float(s[2]),
			'luminosity': float(s[3])}

print '%-20s %-10s %-20s %-10s' % ('Name', 'Distance', 
				'Apparent Brightness', 'Luminosity')
for s in stars:
	print '%-20s %-10.1f %-20f %10f' % (s, stars[s]['distance'], 
					stars[s]['apparent brightness'],
					stars[s]['luminosity'])
 
'''
Name                 Distance   Apparent Brightness  Luminosity
Wolf 359             7.7        0.000001               0.000020
Alpha Centauri C     4.2        0.000010               0.000060
Alpha Centauri B     4.3        0.077000               0.450000
Alpha Centauri A     4.3        0.260000               1.560000
Luyten 726-8 A       8.4        0.000003               0.000060
Sirius B             8.6        0.001000               0.003000
Sirius A             8.6        1.000000              23.600000
Luyten 726-8 B       8.4        0.000002               0.000040
BD +36 degrees 2147  8.2        0.000300               0.006000
Barnard's Star       6.0        0.000040               0.000500
Ross 154             9.4        0.000020               0.000500
'''
