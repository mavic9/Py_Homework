import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 101)
y = 2*(x+2)**2 - 3
y2 = -3*x**2 + 2
y3 = -2*(x-1)**2 + 1
plt.ylim(-5, 5)
plt.plot(x,y, color = "orange")
plt.plot(x,y2, color = "blue")
plt.plot(x, y3, color = "gray")
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['2*(x+2)**2-3','-3*x**2+2', '-2*(x-1)**2+1'])
plt.show()
