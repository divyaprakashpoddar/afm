import numpy as np
import random
from matplotlib import pyplot as plt

x = np.linspace(50,80,100)
u_bar = 100/np.power(x, 1.4)

# Superimpose a fluctuation
for i in range(len(x)):
        r_n = 0.001*random.randrange(-50,50)
        print(r_n)
        u_bar[i] = u_bar[i] + r_n

plt.xlabel('Time')
plt.ylabel('Velocity')
plt.grid()        
plt.plot(x, u_bar)
plt.show()
