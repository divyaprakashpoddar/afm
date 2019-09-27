import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import spline

nu = 1.25e-3
u_mean = np.loadtxt('u_mean')
y = np.loadtxt('y')
u_star = np.sqrt(nu*u_mean[0]/y[0])

# create values of u+
u_plus = u_mean/u_star

# create values of y+
y_plus = y*u_star/nu

plt.figure(1)

plt.semilogx(y_plus,u_plus)
# Smooth Line
#y_plus_new = np.linspace(y_plus.min(), y_plus.max(), 5000)
#u_plus_smooth = spline(y_plus, u_plus, y_plus_new)
#plt.semilogx(y_plus_new,u_plus_smooth)
#plt.semilogx(np.arange(0,20), np.arange(0,20))
#plt.semilogx(y_plus, 2.5*np.log(y_plus) + 2.5)
        
#plt.plot(np.arange(0,20), np.arange(0,20))
#plt.plot(y_plus,u_plus)
#plt.plot(y_plus, 2.5*np.log(y_plus) + 2.5)

plt.xlabel('$y^+$')
plt.ylabel('$u^+$')

plt.xlim(1,1000)
plt.ylim(0)
#plt.figure(2)
#plt.plot(u_mean, y)
plt.grid(True, which = 'both')
plt.show()

