import numpy as np

k, n = 0, 100

a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)

x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
# print(a, b, c, d)
# print(x)
print(k, n, k/n)

# Count of probability using binomial distribution
a = 2
b = 4
p = (np.math.factorial(b)/(np.math.factorial(b-a)*np.math.factorial(a)))*(0.5**a)*(0.5**(b-a))
print(f'The probability of success coin flipping: {p}')

# Count of probability for new k and new n
new_k = 5
new_n = 10
p2 = (np.math.factorial(new_n)/(np.math.factorial(new_n-new_k)*np.math.factorial(new_k)))*(0.5**new_k)*(0.5**(new_n-new_k))
print(f'The probability of success coin flipping for k = {new_k} and n = {new_n}: {p2}')
