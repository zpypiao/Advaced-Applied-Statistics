import numpy as np


mu = np.mat([2, -3, 1]).T

sigma = np.mat([[25, -2, 4],
                [-2, 4, 1],
                [4, 1, 9]])

c = np.mat([3, -2, 1])

c2 = c.T
print(c2)


t1 = np.dot(c, sigma)

t2 = np.dot(t1, c2)
print(t2)

print(1/(np.sqrt(25*15/4)))