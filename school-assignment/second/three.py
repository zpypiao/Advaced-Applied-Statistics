import numpy as np


sig = np.eye(4)*3

a = np.mat([[1, -1, 0, 0],
           [1, 1, -2, 0],
           [1, 1, 1, -3]])

ax = np.dot(np.dot(a, sig), a.T)

print(ax)