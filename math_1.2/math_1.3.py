import numpy as np
import matplotlib.pyplot as plt

# plot circle
fig1 = plt.figure(1)
x = np.linspace(-2, 2, 400)
y = np.sqrt(4 - x**2)
y2 = -np.sqrt(4 - x**2)
plt.plot(x,y, color = 'steelblue')
plt.plot(x, y2, color = 'steelblue')
# plt.gca().set_aspect('equal', adjustable='box')
plt.axis('square')
plt.grid(True)
plt.title('Circle', fontsize = 16)

# plot ellipse
fig2 = plt.figure(2)
x1 = np.linspace(-2, 2, 1000)
y3 = np.sqrt(2*(4 - (x1)**2))
y4 = -np.sqrt(2*(4 - (x1)**2))
plt.plot(x1, y3, color = 'steelblue')
plt.plot(x1, y4, color = 'steelblue')
plt.axis('square')
plt.grid(True)
plt.title('Ellipse', fontsize = 16)

# plot hyperbola
fig3 = plt.figure(3)
x2 = np.linspace(-6, -2, 400)
x3 = np.linspace(2, 6, 400)
y5, y6 = np.sqrt(0.25*(x2**2 - 4)), np.sqrt(0.25*(x3**2 - 4))
y7, y8 = -np.sqrt(0.25*(x2**2 - 4)), -np.sqrt(0.25*(x3**2 - 4))
plt.plot(x2, y5, color = 'steelblue')
plt.plot(x3, y6, color = 'steelblue')
plt.plot(x2, y7, color = 'steelblue')
plt.plot(x3, y8, color = 'steelblue')
plt.axis('square')
plt.grid(True)
plt.title('Hyperbola', fontsize = 16)
plt.show()
