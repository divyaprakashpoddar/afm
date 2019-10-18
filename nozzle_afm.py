# Compressible Flow Nozzle Design
# Author: Divyaprakash

import numpy as np
import matplotlib.pyplot as plt

# Pressure Distribution
P = np.arange(200,1400,10)
N = len(P)

# Flow Properties
m_dot   = 3                     # Unit: kg/s

# Ideal Gas Properties
C_p     = 0.846                 # Unit: kJ/kg/K
gamma   = 1.289
R       = 0.1889 

# Stagnation Properties
T_0     = 473                   # Unit: K
P_0     = 1400                  # Unit: kPa

# Properties
T       = np.zeros(N)           # Temperature
V       = np.zeros(N)           # Velocity
rho     = np.zeros(N)           # Density
A       = np.zeros(N)           # Flow Area
a       = np.zeros(N)           # Speed of Sound
M       = np.zeros(N)           # Mach Number

for i in range(0,N):
        T[i]       = T_0 * np.power((P[i] / P_0), (gamma - 1) / gamma)
        V[i]       = np.sqrt(2 * C_p * (T_0 - T[i]))
        rho[i]     = P[i] / (R * T[i])
        A[i]       = m_dot / (rho[i] * V[i])
        a[i]       = np.sqrt(gamma * R * T[i])
        M[i]       = V[i] / a[i]
        
plt.figure('Pressure v/s Temperature')
plt.plot(P, T)
plt.gca().invert_xaxis()
plt.grid()

plt.figure('Pressure v/s Velocity')
plt.plot(P, V)
plt.gca().invert_xaxis()
plt.grid()

plt.figure('Pressure v/s Density')
plt.plot(P, rho)
plt.gca().invert_xaxis()
plt.grid()

plt.figure('Pressure v/s Area')
plt.plot(P, A)
plt.gca().invert_xaxis()
plt.grid()


plt.figure('Pressure v/s Speed of Sound')
plt.plot(P, a)
plt.gca().invert_xaxis()
plt.grid()

plt.figure('Pressure v/s Mach Number')
plt.plot(P, M)
plt.gca().invert_xaxis()
plt.grid()

plt.show()
