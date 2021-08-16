import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.sin(1.5*x), label='sin(1.5x)')
plt.legend()
plt.show()
