from scitools.std import *
F = linspace(-20,120,100)
f2c_approx = lambda F: (F - 30)/2.0
f2c_exact = lambda F: (F - 32)*5.0/9
C_approx = f2c_approx(F)
C_exact = f2c_exact(F)

plot(F, C_approx, '-')
hold('on')
plot(F, C_exact, '--')
xlabel('Degrees (F)')
ylabel('Degrees (C)')
title('Fahrenheit vs Celsius')
legend('approximate', 'exact conversion')
raw_input('Press Enter to exit: ')

