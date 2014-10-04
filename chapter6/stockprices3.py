import sys

usage = '%s *.csv [*.csv] [...]' % sys.argv[0]

filenames = []
try:
	filenames.append(sys.argv[1])
	for i in sys.argv[2:]:
		filenames.append(i)
except:
	print usage
	sys.exit(1)

def read_file(filename):
    infile = open(filename, 'r')
    infile.readline()  # read column headings
    dates = [];  prices = []
    for line in infile:
        columns = line.split(',')
        date = columns[0]
        date = date[:-3]  # skip day of month
        price = columns[-1]
        dates.append(date)
        prices.append(float(price))
    infile.close()
    dates.reverse()
    prices.reverse()
    return dates, prices

from scitools.std import *

company = {}
for f in filenames:
	name = f.split('_')[-1].split('.')[0]
		# this extracts company from stockprices_company.csv
	dates, prices = read_file(f)
	company[name] = {'dates': dates, 'prices': prices}

figure()
hold('on')
for name in company:
	y = array(company[name]['prices'])/float(company[name]['prices'][0])
		# we want to norm the prices
	x = range(len(y))
	plot(x,y) # this might clobber data
	legend('%s' % name)

raw_input('Press Enter to quit: ')


'''
check out the graphs with
python stockprices3.py stockprices_Microsoft.csv stockprices_Sun.csv
'''
