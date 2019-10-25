# Fanno Flow/ Fanno Line
# Author: Divyaprakash

import numpy as np
import matplotlib.pyplot as plt

# Fluid Properties
R       = 287
Cp      = 1005
gamma   = 1.4

# Upstream Flow Properties
T1      = 500
p1      = 600000
rho1    = 1.002
s1      = 0

a1 = np.sqrt(gamma * R * T1)
V1      = 80
M1 = V1 * a1

# Downstream Temperature
T2 = np.arange(200,600,5)
N = len(T2)

# Properties
p2       = np.zeros(N)           
rho2     = np.zeros(N)           
V2       = np.zeros(N)           
F        = np.zeros(N)           
s2       = np.zeros(N)           
a2       = np.zeros(N)           
M2       = np.zeros(N)           

for i in range(0,N):
        V2[i]   =np.sqrt(2 * Cp * (T1 - T2[i] + V1 * V1 / (2 * Cp)))
        rho2[i] = rho1 * V1 / V2[i]
        p2[i]   = rho2[i] * T2[i] * p1 / (rho1 * T1)
        s2[i]   = s1 + Cp * np.log(T2[i] / T1) - R * np.log(p2[i] / p1)
        F[i]    = p1 - p2[i] + rho1 * V1 * V1 - rho2[i] * V2[i] * V2[i]         

        a2[i]   = np.sqrt(gamma * R * T2[i])
        M2[i]   = V2[i] / a2[i]
        
plt.figure('Entropy v/s Temperature')
plt.plot(s2, T2)
plt.scatter(s2, T2)
plt.grid()

plt.show()
