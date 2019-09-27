import numpy as np
from matplotlib import pyplot as plt

U = np.loadtxt('u_vel')
y = np.loadtxt('y')
u_mean = np.loadtxt('u_mean')

for i in range(0,10):
        plt.figure(1)
        plt.plot(U[:,i], y, alpha = 1)

plt.figure(2)
plt.plot(u_mean, y)

plt.show()
