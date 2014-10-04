from numpy import *
random.seed(1)

N = 20
r = random.uniform(0,1,N)

print 'r <= 0.5:'
print r <= 0.5
print 'r[r <= 0.5]'
print r[r <= 0.5]
print 'where(r <= 0.5, 1, 0)'
print where(r <= 0.5, 1, 0)

print 'Number of elements less than or equal to 0.5 = ', sum(r <= 0.5)

'''
python bool_vec.py
r <= 0.5:
[ True False  True  True  True  True  True  True  True False  True False
  True False  True False  True False  True  True]
r[r <= 0.5]
[  4.17022005e-01   1.14374817e-04   3.02332573e-01   1.46755891e-01
   9.23385948e-02   1.86260211e-01   3.45560727e-01   3.96767474e-01
   4.19194514e-01   2.04452250e-01   2.73875932e-02   4.17304802e-01
   1.40386939e-01   1.98101489e-01]
where(r <= 0.5, 1, 0)
[1 0 1 1 1 1 1 1 1 0 1 0 1 0 1 0 1 0 1 1]
Number of elements less than or equal to 0.5 =  14
'''
