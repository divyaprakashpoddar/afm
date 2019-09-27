import numpy as np
from matplotlib import pyplot as plt


r = np.linspace(-1,1,100)
R = 1
u_avg = 1

u_r = 2 * u_avg * (1 - r*r/(R*R) )

plt.plot(u_r, r)
plt.ylim(-1,0)
plt.xlabel('u(r)')
plt.ylabel('r')

plt.show()
