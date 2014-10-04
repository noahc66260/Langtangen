#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
_ip.magic("logstart ")

a = []
a
b = [1, 4.4, 'run.py']
b
a.append(5)
a
a + [1,3]
a.insert(0, 100)
a
a[1]
a[-1]
a[-2]
a[0:2]
del a[0]
a
a.remove(5)
a
b.index('run.py')
b[2]
b = b + [1,2,3]
b
b.count(1)
len(b)
min(b)
max(b)
sorted(b)
b
reverse(b)
isinstance(b,1)
isinstance(1,b)
1 in b
isinstance(b, list)
isinstance(1, int)
isinstance(b,int)
_ip.magic("logoff ")
