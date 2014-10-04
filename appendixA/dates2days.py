import datetime

date1 = datetime.date(2009, 1, 4)
date2 = datetime.date(2009, 3, 21)
date3 = datetime.date(2009, 4, 1)
date4 = datetime.date(2009, 6, 30)
date5 = datetime.date(2009, 11, 1)
date6 = datetime.date(2010, 4, 1)


year1 = 2009
month1 = 7
day1 = 16

year2 = 2010
month2 = 2
day2 = 13

start = datetime.date(year1, month1, day1)
end = datetime.date(year2, month2, day2)
duration = (end - start).days
p = zeros(duration)

default = 4.0
for i in range(duration):
	if (start - date6).days >= 0:
		p[i] = 2.0
	elif (start - date5).days >= 0:
		p[i] = 4.5
	elif (start - date4).days >= 0:
		p[i] = 5.0
	elif (start - date3).days >= 0:
		p[i] = 2.0
	elif (start - date2).days >= 0:
		p[i] = 4.5
	elif (start - date1).days >= 0:
		p[i] = 5.0
	else:
		p[i] = default

