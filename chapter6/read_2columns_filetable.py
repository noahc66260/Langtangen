from scitools.std import *
import scitools.filetable as ft

infile = open('xy.dat', 'r')
x, y = ft.read_columns(infile)
infile.close()

print 'The maximum y coordinate is %6.4f' % max(y)
print 'The minimum y coordinate is %6.4f' % min(y)
plot(x,y, xlabel='x', ylabel='y')
raw_input('Press Enter to quit: ')

'''
python read_2columns_filetable.py
The maximum y coordinate is 0.9482
The minimum y coordinate is -0.9482
Press Enter to quit: 
'''
