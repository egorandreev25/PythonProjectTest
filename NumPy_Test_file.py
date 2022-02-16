import numpy as np
from matplotlib import pyplot as plt

# defining X with inout from Terminal
x_array = np.array([3, -8]).reshape(2,1)
print(x_array)
# defining A with randomize
a_array = np.linspace(0, 10, 1000)
a = np.vstack((np.sin(a_array), np.cos(a_array))).T

# Multiplication A*X
b = a @ x_array
# printing b after Multiplication

# creating the noise (Gaus distribution)
noise = np.random.normal(0, 0.1, (len(b), b.ndim))

# square roots solve
ata = a.T @ a
atb = a.T @ b
x_hat = np.linalg.solve(a=ata, b=atb)
print('Estimated Parameters are: ', x_hat)

plt.plot(b + noise, 'k.')
plt.title("A linear regression task")
plt.plot(a @ x_hat, 'r:')
plt.legend(["Noisy data", "Least squares estimate"])
plt.show()
