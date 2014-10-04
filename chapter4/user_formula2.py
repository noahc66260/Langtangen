from scitools.StringFunction import StringFunction
formula = raw_input('Write a formula involving x: ')
f = StringFunction(formula)

x = 0
while x is not None: 
    x = eval(raw_input('Give x (None to quit): '))
    if x is not None:
        print 'f(%g)=%g' % (x, f(x))
   
