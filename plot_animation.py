import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


X, Y = np.meshgrid(np.arange(-1, 5, 0.5), np.arange(-1, 5, 0.5))
omega = 2 * np.pi
t = 1

U = 0.5 + 0.8 * X
V = 1.5 + 2.5 * np.sin(omega * t) - 0.8 * Y


fig, ax = plt.subplots()
Q = ax.quiver(X, Y, U, V)

ax.set_xlim(0, 4)
ax.set_ylim(-1, 4)


def update_quiver(num, Q, X, Y):

    U = 0.5 + 0.8 * X
    V = 1.5 + 2.5 * np.sin(omega * num/100) - 0.8 * Y

    Q.set_UVC(U, V)
    return Q


ani = FuncAnimation(fig, update_quiver, fargs=(Q, X, Y), interval=1, blit=False)

plt.show()
