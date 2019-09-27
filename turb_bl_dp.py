import matplotlib.pyplot as plt
import numpy as np
import math
import random
import pyJHTDB
import time as tt
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import filters
import skimage.morphology as morphology
from skimage.morphology import square
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from matplotlib import cm

# load shared library
lTDB = pyJHTDB.libJHTDB()
#initialize webservices
lTDB.initialize()

#Add token
auth_token  = "edu.jhu.pha.turbulence.testing-201311"  #Replace with your own token here
lTDB.add_token(auth_token)

dataset = 'transition_bl'

spatialInterp  = 0  # no spatial interpolation
temporalInterp = 0  # no time interpolation
FD4NoInt       = 40 # 4th-order FD, no spatial interpolation

# Database domain size and number of grid points
x_min =   30.2185
x_max = 1000.0650
#y_min =    0.0036
y_min =    0
#y_max =   26.4880
y_max = 15
z_min =    0.0000
z_max =  240.0000
d99i  =    0.9648
d99f  =   15.0433

nx = 1
ny = 500
nz = 1

# Database time duration
Ti = 0
Tf = Ti + 1175
dt = 0.25

# Create surface
nix = round(nx)
niy = round(ny)
x = 900
y = np.linspace(y_min, y_max, niy)
z = 50

[X,Y] = np.meshgrid(x,y)
points = np.zeros((nix,niy,3))
points[:,:,0] = 900
points[:,:,1] = y.transpose()
points[:,:,2] = 50

# 2D array with single precision values
points = np.array(points,dtype='float32')

time = Ti
U = np.zeros((niy,50))

for t in range(0, 50):
        start = tt.time()
        print('Requesting velocity at {0} points...'.format(nix*niy))
        result = lTDB.getData(t, points, data_set = 'transition_bl',
        sinterp = spatialInterp, tinterp = temporalInterp,
        getFunction = 'getVelocity')
        end = tt.time()
        U[:,t] = result[:,:,0]
        print('   '+str(end - start)+' seconds')
        plt.plot(U[:,t],y,alpha=0.25)
        tt.sleep(1)

        #start = tt.time()
        #print('Requesting velocity gradients at {0} points...'.format(nix*niy))
        #result_grad = lTDB.getData(t, points, data_set = 'transition_bl',
        #sinterp = FD4NoInt, tinterp = temporalInterp,
        #getFunction = 'getVelocityGradient')
        #end = tt.time()

np.savetxt('u_vel',U)
u_mean = U.sum(axis=1)/(50)
np.savetxt('u_mean', u_mean)
np.savetxt('y', y)
#tt.sleep(5)
plt.plot(u_mean,y,linewidth=2)
#plt.semilogx(y,u_mean,linewidth=2)
plt.show()


