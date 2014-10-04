# converts 10**9 seconds to years

seconds = 10**9
secondsPerMinute = 60
minutesPerHour = 60
hoursPerDay = 24
daysPerYear = 365

years = float(seconds) / secondsPerMinute / minutesPerHour \
     / hoursPerDay / daysPerYear

print "%g seconds is %g years" % (seconds, years)

'''
python seconds2years.py
1e+09 seconds is 31.7098 years
'''
