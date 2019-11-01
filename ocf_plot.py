# Best Hydraulic Cross-section (Rectangular)
# Author: Divyaprakash

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Channel Parameters
S       = np.tan(np.deg2rad(1))         # Slope of the channel
A       = 1                             # Cross-Sectional Area
n       = 0.012                         # Roughness Coefficient

# Aspect ratios
Ratios = np.linspace(0.1,1.5,50)        # ar = y / b

# Plots Setup
fig1, ax1 = plt.subplots()
plt.grid(axis = 'both')
ax1.set_xlabel('Aspect Ratio (y/b)')
ax1.set_ylabel('Flow Rate')

ax2 = ax1.twinx()
ax2.set_ylabel('Wetted Perimeter')

fig2, ax3 = plt.subplots()
plt.grid(axis = 'both')
ax3.set_xlabel('Aspect Ratio (y/b)')
ax3.set_ylabel('Hydraulic Radius $R_h$')

# Flow rate calculation for various aspect ratios
for ar in Ratios: 
        def equations(p):
                y, b    = p
                return (y * b - A, y - ar * b)

        y, b    = fsolve(equations, (1,1))

        Pw      = 2 * y + b               # Wetted Perimeter
        Rh      = A / Pw                  # Hydraulic Radius
        Q       = (1 / n) * A * np.power(Rh, (2/3)) * np.power(S, (1/2))

        ax1.scatter(ar, Q, color = 'k')
        ax2.scatter(ar, Pw, color = 'b')
        ax3.scatter(ar, Rh, color = 'c')         


fig.tight_layout()
plt.show()



