import numpy as np
import matplotlib.pyplot as plt

# plot circle
fig1 = plt.figure(1)
x = np.linspace(0, 2*np.pi, 360)
y = [3]*360
plt.polar(x,y)
plt.title('Circle', fontsize = 16)

# plot segment
fig2 = plt.figure(2)
x1 = [np.pi/4]*100
y1 = np.linspace(0, 3, 100)
plt.polar(x1, y1)
plt.title('Line segment', fontsize = 16)
plt.show()
