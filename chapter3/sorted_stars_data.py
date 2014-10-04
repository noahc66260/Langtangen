data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005),
]

def sortDistance(a,b):
	'''
	Sorting function for the 4-tuple by distance
	'''
	if a[1] < b[1]:
		return -1
	elif a[1] > b[1]:
		return 1
	else:
		return 0

def sortBrightness(a,b):
	'''
	Sorting function for the 4-tuple by apparent brightness
	'''
	if a[2] < b[2]:
		return -1
	elif a[2] > b[2]:
		return 1
	else:
		return 0

def sortLuminosity(a,b):
	'''
	Sorting function for the 4-tuple by luminosity
	'''
	if a[2] < b[2]:
		return -1
	elif a[2] > b[2]:
		return 1
	else:
		return 0

print 'First we sort by distance...'
print '%20s %10s' % ('Star Name', 'Distance')
a = sorted(data, sortDistance)
for i in a:
	print '%20s %10.1f' % (i[0], i[1])
print ''

print 'Next we sort by brightness...'
print '%20s %10s' % ('Star Name', 'Brightness')
a = sorted(data, sortBrightness)
for i in a:
	print '%20s %10f' % (i[0], i[2])
print ''

print 'Next we sort by luminosity...'
print '%20s %10s' % ('Star Name', 'Luminosity')
a = sorted(data, sortLuminosity)
for i in a:
	print '%20s %10f' % (i[0], i[3])
print ''
