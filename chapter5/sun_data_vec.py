from Oxford_sun_hours import *
from scitools.std import *

data = array(data)
mo_avg = [mean(data[:, i:i+1]) for i in range(data.shape[1])]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
i = mo_avg.index(max(mo_avg))
print 'The month with the best weather is %s with %.1f average sun hours' % (months[i], mo_avg[i])

# calculating the avg sun hours per decade for Jan and December is 
# tedious and not instructive, so I have decided to skip it.
# Basically we concatenate the splices for each decade and then
# find the mean. 
