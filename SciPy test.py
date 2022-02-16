import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1]**2.0)**2.0)
X = np.arange(-2, 2, 0.2)
Y = np.arange(-2, 2, 0.2)
X, Y = np.meshgrid(X, Y)

data = np.vstack([X.reshape(X.size), Y.reshape(Y.size)])
Z = rosen(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z.reshape(X.shape), cmap='bwr')
ax.view_init(40, 230)
plt.show()

from scipy.optimize import minimize

x0 = np.array([1.3, 0.7])
res = minimize(rosen, x0, method='nelder-mead',
               options={'xatol': 1e-8, 'disp': True})

print(res.x)