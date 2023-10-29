import numpy as np

from sklearn.preprocessing import StandardScaler

data = np.array([[25, 7, 2.5],
               [18, 6, 2.2],
               [23, 7, 2.3]])

# mean
m = np.mean(data, 0)
# [22.          6.66666667  2.33333333]

# A(x)
data_ = data - m
# [[ 3.          0.33333333  0.16666667]
#  [-4.         -0.66666667 -0.13333333]
#  [ 1.          0.33333333 -0.03333333]]

a = np.dot(data_, data_.T)

print(a)


transfer = StandardScaler()
data_new = transfer.fit_transform(data)
print(data_new)