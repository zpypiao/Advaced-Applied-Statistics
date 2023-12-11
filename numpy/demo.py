# This is a python program which is used by learning
# written by zhaopiaoyang

import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4])

# command copy is a deep copy
x = arr.copy()

# command view is a light copy
y = arr.view()

# change the original array
arr[0] = 5

# reshape is a view, and the array will be flatted if use the command "arr.reshape(-1)"
z = arr.reshape(2, 2)

url = 'https://github.com/zpypiao/Advaced-Applied-Statistics/blob/main/data/data_one.xlsx'

data = pd.read_excel(url, sheet_name='sheet1')

print(data.head(10))