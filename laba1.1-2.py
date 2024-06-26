import numpy as np

A = np.array([[1, 2, 3],
              [3, 2, 1],
              [2, 3, 1]])
V = np.array([[1],
              [1],
              [1]])

L = np.dot(A, V)
print(f'Умножение:\n{L}'
      f'\nСумма значений:\n {np.add.reduce(L)}')



