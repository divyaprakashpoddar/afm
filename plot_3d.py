import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X, Y, Z = np.meshgrid(np.arange(0, 2, 0.5), np.arange(0, 2, 0.5), np.arange(0, 2, 0.5))

U = X * X * Y
V = Y * Y * Z
W = -X * Y * Z - Y * Z * Z

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.quiver(X, Y, Z, U, V, W, length=0.2, normalize=True)

plt.show()

