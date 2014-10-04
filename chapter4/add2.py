import sys
from math import *
i1 = eval(sys.argv[1])
i2 = eval(sys.argv[2])
r = i1 + i2
print '%s + %s becomes %s\nwith value %s' % \
      (type(i1), type(i2), type(r), r)

'''
python add2.py 'sqrt(2)' 'sin(1.2)'
<type 'float'> + <type 'float'> becomes <type 'float'>
with value 2.34625264834
'''
