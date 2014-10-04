import numpy as np
x = np.linspace(0,2,20)
x2 = np.linspace(0,2,1000)
y2 = np.cos(18*np.pi*x2)
y = np.cos(18*np.pi*x)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.hold('on')
plt.plot(x2,y2)
plt.show()

