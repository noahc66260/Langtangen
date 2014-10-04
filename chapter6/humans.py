filename = 'human_evolution.txt'
infile = open(filename, 'r')
for i in range(3):
	infile.readline() # discard first three lines

humans = {}
for line in infile:
	if 'H. ' not in line:
		continue
	name = line[:21].strip()
	when = line[21:37].strip()
	height = line[37:50].strip()
	weight = line[50:62].strip()
	brain_volume = line[62:].strip()
	humans[name] = {}
	humans[name]['when'] = when
	humans[name]['height'] = height
	humans[name]['weight'] = weight
	humans[name]['brain volume'] = brain_volume
infile.close()

print '%-21s %-16s %-13s %-12s %-s' % ('Species', 'Lived when',
				'height', 
				'mass', 
				'Brain volume')
print '%-21s %-16s %-13s %-12s %-s' % ('', '(mill. yrs)', '(m)',
				'(kg)', '(cm**3)')

for name in sorted(humans):
	print '%-21s %-16s %-13s %-12s %-s' % (name,
					humans[name]['when'],
					humans[name]['height'],
					humans[name]['weight'],
					humans[name]['brain volume'])
