import calendar
import sys
usage = '%s year month day\nyear is four digits, month is two digits, day is two digits' % (sys.argv[0])
try:
	year = eval(sys.argv[1])
	month = eval(sys.argv[2])
	day = eval(sys.argv[3])
except:
	print usage
	sys.exit(1)
i = calendar.weekday(year, month, day)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print 'On %d/%d/%d it is a %s' % (day, month, year, weekdays[i])

'''
python weekday.py 2012 8 15
On 15/8/2012 it is a Wednesday
'''
