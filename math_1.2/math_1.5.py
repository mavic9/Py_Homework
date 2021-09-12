from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# plot two parallel planes
fig = figure(1)
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = X + 2 * Y
Z1 = X + 2 * Y + 25
ax.plot_wireframe(X, Y, Z)  # ax.plot_surface(X, Y, Z)
ax.plot_wireframe(X, Y, Z1)

# plot paraboloid
fig = figure(2)
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.01)
Y = np.arange(-4, 4, 0.01)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(1 + X ** 2 + Y ** 2)
Z1 = -np.sqrt(1 + X ** 2 + Y ** 2)
ax.plot_surface(X, Y, Z, color='steelblue')  # ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z1, color='steelblue')

# plot spheroid
fig = figure(3)
ax = Axes3D(fig)
X = np.arange(-3, 3, 0.01)
Y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt(9 - X ** 2 - Y ** 2)
Z1 = -np.sqrt(9 - X ** 2 - Y ** 2)
ax.plot_surface(X, Y, Z, color='steelblue')  # ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z1, color='steelblue')
plt.show()
