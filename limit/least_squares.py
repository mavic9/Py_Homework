from matplotlib import pylab as plt
import numpy as np

# Задаем рандомное распределение точек
xi = np.random.uniform(-8, 8, 200)
yi = 1/(1+np.exp(-np.random.uniform(0.5, 1.5, 200)*xi-np.random.uniform(-1, 1, 200)))
plt.plot(xi,yi, marker="o", ls="")

x = np.linspace(-8, 8, 200)
y=1/(1+2.7182818**(-x))

# сигмоидальная функция для a = 1 и b = 0
x = np.linspace(-8, 8, 200)
y=1/(1+2.7182**((-x)))


plt.plot(x,y, c='r')
plt.show()

plt.show()

y_=y.sum()/200

r=np.sqrt((((yi-y_)**2).sum()-((yi-(1/(1+2.7182**(-(xi)))))**2).sum())/((yi-y_)**2).sum())

print(r)
